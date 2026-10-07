import { makeNotice } from '../notice.js';
import { fetchJson } from '../http.js';

/**
 * UK Find a Tender (FTS) and Contracts Finder both publish OCDS release
 * packages with cursor pagination via `links.next`. Only tender-stage releases
 * are kept; awards/contracts are a different product.
 */
export const UK_SOURCES = {
    'uk-fts': {
        firstPage: (since) => `https://www.find-tender.service.gov.uk/api/1.0/ocdsReleasePackages?updatedFrom=${since.toISOString().slice(0, 19)}&limit=100&stages=tender`,
        noticeUrl: (r) => `https://www.find-tender.service.gov.uk/Notice/${r.id}`,
    },
    'uk-cf': {
        firstPage: (since) => `https://www.contractsfinder.service.gov.uk/Published/Notices/OCDS/Search?publishedFrom=${since.toISOString().slice(0, 10)}&stages=tender&limit=100`,
        noticeUrl: (r) => `https://www.contractsfinder.service.gov.uk/Notice/${r.id}`,
    },
};

export async function* fetchOcds(source, { since, maxPages = 50, log }) {
    const cfg = UK_SOURCES[source];
    let url = cfg.firstPage(since);
    for (let page = 0; url && page < maxPages; page++) {
        const pkg = await fetchJson(url, { log });
        for (const release of pkg.releases ?? []) {
            if (!isTenderStage(release)) continue;
            yield normalizeOcdsRelease(source, release, cfg.noticeUrl(release));
        }
        url = pkg.links?.next ?? null;
    }
}

function isTenderStage(release) {
    const tags = release.tag ?? [];
    return tags.length === 0 || tags.some((t) => t === 'tender' || t === 'tenderUpdate' || t === 'planning');
}

export function normalizeOcdsRelease(source, r, url) {
    const t = r.tender ?? {};
    const buyerParty = (r.parties ?? []).find((p) => p.roles?.includes('buyer')) ?? r.buyer ?? {};
    const classifications = [t.classification, ...(t.items ?? []).flatMap((i) => [i.classification, ...(i.additionalClassifications ?? [])])].filter(Boolean);
    const cpv = classifications.filter((c) => /cpv/i.test(c.scheme ?? 'CPV')).map((c) => String(c.id).split('-')[0]);
    return makeNotice({
        source,
        // ocid is stable across a notice's updates; release.id changes per release.
        sourceId: r.ocid ?? r.id,
        url,
        title: t.title ?? r.title,
        // Find a Tender often puts only a one-line summary in tender.description
        // and the substance in the lots.
        description: [t.description, ...(t.lots ?? []).map((l) => l.description)].filter(Boolean).join('\n\n'),
        buyerName: buyerParty.name ?? r.buyer?.name,
        country: countryCode(buyerParty.address?.countryName) ?? 'GB',
        noticeType: (r.tag ?? []).join(','),
        status: t.status,
        publishedAt: r.date,
        deadlineAt: t.tenderPeriod?.endDate,
        value: t.value ?? (t.minValue ? { amount: t.minValue.amount, currency: t.minValue.currency } : null),
        cpv,
        placeOfPerformance: t.deliveryAddresses?.[0]?.region ?? t.items?.[0]?.deliveryAddresses?.[0]?.region,
    });
}

function countryCode(name) {
    if (!name) return null;
    if (/^[A-Z]{2}$/i.test(name)) return name.toUpperCase();
    return /united kingdom|england|scotland|wales|northern ireland|great britain/i.test(name) ? 'GB' : null;
}
