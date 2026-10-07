import { makeNotice } from '../notice.js';
import { fetchJson } from '../http.js';

const BASE = 'https://api.sam.gov/opportunities/v2/search';
// Pre-award notice types only (o=solicitation, p=presolicitation, k=combined synopsis/solicitation, r=sources sought).
const PTYPES = 'o,p,k,r';

function mmddyyyy(d) {
    return `${String(d.getUTCMonth() + 1).padStart(2, '0')}/${String(d.getUTCDate()).padStart(2, '0')}/${d.getUTCFullYear()}`;
}

/**
 * SAM.gov requires a personal api.data.gov key with a low daily cap, so the
 * key is supplied by each user rather than shared across all runs.
 */
export async function* fetchSam({ since, apiKey, naicsPrefixes = [], maxPages = 10, log }) {
    const limit = 1000;
    // SAM filters by exact 6-digit NAICS only; prefixes are applied client-side.
    const exactNaics = naicsPrefixes.length === 1 && naicsPrefixes[0].length === 6 ? `&ncode=${naicsPrefixes[0]}` : '';
    for (let page = 0; page < maxPages; page++) {
        const url = `${BASE}?api_key=${encodeURIComponent(apiKey)}&postedFrom=${mmddyyyy(since)}&postedTo=${mmddyyyy(new Date())}&ptype=${PTYPES}&limit=${limit}&offset=${page * limit}${exactNaics}`;
        const res = await fetchJson(url, { log });
        const rows = res.opportunitiesData ?? [];
        for (const raw of rows) yield normalizeSamOpportunity(raw);
        if (rows.length < limit) break;
    }
}

export function normalizeSamOpportunity(raw) {
    const award = raw.award?.amount ?? null;
    return makeNotice({
        source: 'sam',
        sourceId: raw.noticeId,
        url: raw.uiLink ?? `https://sam.gov/opp/${raw.noticeId}/view`,
        title: raw.title,
        // `description` is a URL to a separate endpoint that needs the key; not fetched to save quota.
        description: [raw.solicitationNumber && `Solicitation ${raw.solicitationNumber}`, raw.typeOfSetAsideDescription && `Set-aside: ${raw.typeOfSetAsideDescription}`].filter(Boolean).join('. ') || null,
        buyerName: raw.fullParentPathName?.split('.').map((s) => s.trim()).filter(Boolean).slice(-2).join(' / ') ?? raw.department,
        country: raw.placeOfPerformance?.country?.code === 'USA' || !raw.placeOfPerformance?.country?.code ? 'US' : raw.placeOfPerformance.country.code,
        noticeType: raw.type ?? raw.baseType,
        status: raw.active === 'Yes' ? 'active' : raw.active === 'No' ? 'inactive' : null,
        publishedAt: raw.postedDate,
        deadlineAt: raw.responseDeadLine,
        value: award != null ? { amount: Number(award), currency: 'USD' } : null,
        naics: [].concat(raw.naicsCode ?? raw.naicsCodes ?? []),
        cpv: [],
        placeOfPerformance: [raw.placeOfPerformance?.city?.name, raw.placeOfPerformance?.state?.code].filter(Boolean).join(', ') || null,
    });
}
