// Live integration check against the real portals (run in CI, which has open
// network access). Prints one raw record and its normalized form per source so
// test fixtures and normalizers can be corrected, and fails if a source
// returns nothing or normalizes without the core fields.
import { fetchTed } from '../src/sources/ted.js';
import { fetchOcds } from '../src/sources/ocds.js';
import { fetchSam } from '../src/sources/sam.js';
import { fetchJson } from '../src/http.js';

const since = new Date(Date.now() - 2 * 86_400_000);
const log = { warning: (m) => console.warn(`WARN ${m}`) };
const checks = {
    ted: () => fetchTed({ since, countries: [], maxPages: 1, log }),
    'uk-fts': () => fetchOcds('uk-fts', { since, maxPages: 1, log }),
    'uk-cf': () => fetchOcds('uk-cf', { since, maxPages: 1, log }),
};
if (process.env.SAM_API_KEY) checks.sam = () => fetchSam({ since, apiKey: process.env.SAM_API_KEY, maxPages: 1, log });

const raw = {
    ted: async () => (await fetchJson('https://api.ted.europa.eu/v3/notices/search', {
        method: 'POST',
        body: { query: `publication-date>=${since.toISOString().slice(0, 10).replaceAll('-', '')}`, fields: ['publication-number', 'notice-title', 'buyer-name', 'buyer-country', 'classification-cpv', 'publication-date', 'notice-type', 'deadline-receipt-tender-date-lot', 'estimated-value-lot', 'estimated-value-cur-lot', 'description-lot', 'place-of-performance'], limit: 1 },
    })).notices?.[0],
    'uk-fts': async () => (await fetchJson(`https://www.find-tender.service.gov.uk/api/1.0/ocdsReleasePackages?updatedFrom=${since.toISOString().slice(0, 19)}&limit=1&stages=tender`)),
    'uk-cf': async () => (await fetchJson(`https://www.contractsfinder.service.gov.uk/Published/Notices/OCDS/Search?publishedFrom=${since.toISOString().slice(0, 10)}&stages=tender&limit=1`)),
};

let failed = false;
for (const [source, run] of Object.entries(checks)) {
    console.log(`\n===== ${source} =====`);
    try {
        if (raw[source]) {
            const sample = await raw[source]().catch((e) => `raw fetch failed: ${e.message}`);
            console.log('RAW SAMPLE:', JSON.stringify(sample, null, 1).slice(0, 4000));
        }
        const out = [];
        for await (const n of run()) {
            out.push(n);
            if (out.length >= 200) break;
        }
        const complete = out.filter((n) => n.title !== '(untitled)' && n.url && n.publishedAt);
        console.log(`normalized: ${out.length}, with title+url+publishedAt: ${complete.length}`);
        const fill = (k) => `${k}=${out.filter((n) => (Array.isArray(n[k]) ? n[k].length : n[k] != null)).length}`;
        console.log('field fill:', ['buyerName', 'country', 'deadlineAt', 'value', 'cpv', 'naics', 'description'].map(fill).join(' '));
        console.log('NORMALIZED SAMPLE:', JSON.stringify(out.slice(0, 2), null, 1));
        if (!out.length || complete.length < out.length * 0.9) failed = true;
    } catch (e) {
        console.log(`FAILED: ${e.stack}`);
        failed = true;
    }
}
process.exit(failed ? 1 : 0);
