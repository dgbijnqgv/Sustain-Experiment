import { makeNotice } from '../notice.js';
import { fetchJson } from '../http.js';

const SEARCH_URL = 'https://api.ted.europa.eu/v3/notices/search';
const CORE_FIELDS = ['publication-number', 'notice-title', 'buyer-name', 'buyer-country', 'classification-cpv', 'publication-date', 'notice-type'];
const EXTRA_FIELDS = ['deadline-receipt-tender-date-lot', 'estimated-value-lot', 'estimated-value-cur-lot', 'description-lot', 'place-of-performance'];
// Competition (call for tender) notice subtypes; results/awards are excluded.
const COMPETITION_TYPES = ['cn-standard', 'cn-social', 'cn-desg', 'pin-cfc-standard', 'pin-cfc-social'];

const ISO3_TO_ISO2 = {
    AUT: 'AT', BEL: 'BE', BGR: 'BG', HRV: 'HR', CYP: 'CY', CZE: 'CZ', DNK: 'DK', EST: 'EE', FIN: 'FI', FRA: 'FR', DEU: 'DE', GRC: 'GR',
    HUN: 'HU', IRL: 'IE', ITA: 'IT', LVA: 'LV', LTU: 'LT', LUX: 'LU', MLT: 'MT', NLD: 'NL', POL: 'PL', PRT: 'PT', ROU: 'RO', SVK: 'SK',
    SVN: 'SI', ESP: 'ES', SWE: 'SE', NOR: 'NO', ISL: 'IS', LIE: 'LI', CHE: 'CH', GBR: 'GB', MKD: 'MK', SRB: 'RS', MNE: 'ME', ALB: 'AL', UKR: 'UA',
    MDA: 'MD', GEO: 'GE', TUR: 'TR',
};
const ISO2_TO_ISO3 = Object.fromEntries(Object.entries(ISO3_TO_ISO2).map(([a, b]) => [b, a]));

export function buildTedQuery(since, countries = []) {
    const date = since.toISOString().slice(0, 10).replaceAll('-', '');
    let q = `publication-date>=${date} AND notice-type IN (${COMPETITION_TYPES.join(' ')})`;
    const iso3 = countries.map((c) => ISO2_TO_ISO3[c.toUpperCase()]).filter(Boolean);
    if (iso3.length) q += ` AND buyer-country IN (${iso3.join(' ')})`;
    return q;
}

export async function* fetchTed({ since, countries, maxPages = 100, log }) {
    let fields = [...CORE_FIELDS, ...EXTRA_FIELDS];
    let token = null;
    for (let page = 0; page < maxPages; page++) {
        const body = { query: buildTedQuery(since, countries), fields, limit: 250, scope: 'ACTIVE', paginationMode: 'ITERATION', ...(token ? { iterationNextToken: token } : {}) };
        let res;
        try {
            res = await fetchJson(SEARCH_URL, { method: 'POST', body, log });
        } catch (e) {
            // The optional field list is the most likely thing to drift; fall back once.
            if (e.status === 400 && fields.length > CORE_FIELDS.length) {
                log?.warning(`TED rejected extended field list, falling back to core fields: ${e.message}`);
                fields = CORE_FIELDS;
                page--;
                continue;
            }
            throw e;
        }
        for (const raw of res.notices ?? []) yield normalizeTedNotice(raw);
        token = res.iterationNextToken;
        if (!token || !(res.notices ?? []).length) break;
    }
}

export function normalizeTedNotice(raw) {
    const pub = raw['publication-number'];
    const countryRaw = first(raw['buyer-country']);
    const amount = first(raw['estimated-value-lot']);
    return makeNotice({
        source: 'ted',
        sourceId: pub,
        url: raw.links?.html?.ENG ?? (pub ? `https://ted.europa.eu/en/notice/-/detail/${pub}` : null),
        title: pickLang(raw['notice-title']),
        description: pickLang(raw['description-lot']),
        buyerName: pickLang(raw['buyer-name']),
        country: ISO3_TO_ISO2[countryRaw] ?? countryRaw,
        noticeType: first(raw['notice-type']),
        status: 'active',
        publishedAt: stripTz(first(raw['publication-date'])),
        deadlineAt: stripTz(minDate(raw['deadline-receipt-tender-date-lot'])),
        value: amount != null ? { amount: Number(amount), currency: first(raw['estimated-value-cur-lot']) } : null,
        cpv: [].concat(raw['classification-cpv'] ?? []).map(String),
        placeOfPerformance: [].concat(raw['place-of-performance'] ?? []).slice(0, 3).join(', ') || null,
    });
}

/** TED multilingual values: { eng: 'x' } or { eng: ['x'] }; prefer English. */
function pickLang(v) {
    if (v == null) return null;
    if (typeof v === 'string') return v;
    if (Array.isArray(v)) return pickLang(v[0]);
    const val = v.eng ?? v.ENG ?? Object.values(v)[0];
    return Array.isArray(val) ? val[0] : val;
}

function first(v) {
    return Array.isArray(v) ? v[0] : v ?? null;
}

function minDate(v) {
    const arr = [].concat(v ?? []).filter(Boolean).sort();
    return arr[0] ?? null;
}

// TED dates look like "2026-10-01+02:00"; Date() cannot parse a bare date with offset.
function stripTz(d) {
    if (!d) return null;
    const m = String(d).match(/^(\d{4}-\d{2}-\d{2})(T[\d:.]+)?(Z|[+-]\d{2}:\d{2})?$/);
    if (!m) return d;
    return `${m[1]}${m[2] ?? 'T00:00:00'}${m[3] ?? 'Z'}`;
}
