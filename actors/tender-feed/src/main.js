import { Actor, log } from 'apify';
import { matchesFilters } from './notice.js';
import { ChangeTracker } from './tracker.js';
import { fetchOcds } from './sources/ocds.js';
import { fetchSam } from './sources/sam.js';
import { fetchTed } from './sources/ted.js';

const PUSH_BATCH = 100;

await Actor.init();

const input = (await Actor.getInput()) ?? {};
const {
    sources = ['ted', 'uk-fts', 'uk-cf'],
    keywords = [],
    excludeKeywords = [],
    cpvPrefixes = [],
    naicsPrefixes = [],
    countries = [],
    minValue = null,
    lookbackDays = 3,
    onlyChanges = true,
    watchName = 'default',
    samApiKey = null,
    maxItems = 5000,
} = input;

const since = new Date(Date.now() - lookbackDays * 86_400_000);
const filters = { keywords, excludeKeywords, cpvPrefixes, naicsPrefixes, countries, minValue };

// Named store: persists across runs for the user running the Actor, so each
// watch remembers what it already delivered.
const stateStore = await Actor.openKeyValueStore('tender-feed-state');
const stateKey = `watch-${watchName.replace(/[^a-zA-Z0-9-]/g, '-').slice(0, 60)}`;
const tracker = new ChangeTracker((await stateStore.getValue(stateKey)) ?? {});

const generators = {
    ted: () => fetchTed({ since, countries, log }),
    'uk-fts': () => fetchOcds('uk-fts', { since, log }),
    'uk-cf': () => fetchOcds('uk-cf', { since, log }),
    sam: () => fetchSam({ since, apiKey: samApiKey, naicsPrefixes, log }),
};

const stats = { emitted: 0, new: 0, updated: 0, unchanged: 0, filteredOut: 0, sourceErrors: {} };
const seenThisRun = new Set();
let buffer = [];
let stop = false;

async function flush() {
    if (!buffer.length) return;
    const batch = buffer;
    buffer = [];
    const res = await Actor.pushData(batch, 'notice');
    if (res?.eventChargeLimitReached) {
        // Items past the user's spending cap were not delivered; forget them so
        // the next run returns them instead of treating them as already sent.
        for (const item of batch.slice(res.chargedCount)) tracker.forget(item.id);
        log.info('Reached the maximum cost you set for this run; stopping early.');
        stop = true;
    }
}

for (const source of sources) {
    if (stop) break;
    if (!generators[source]) {
        log.warning(`Unknown source "${source}", skipping.`);
        stats.sourceErrors[source] = 'unknown source';
        continue;
    }
    if (source === 'sam' && !samApiKey) {
        log.warning('Skipping SAM.gov: provide a free api.data.gov key in "samApiKey" (https://open.gsa.gov/api/get-opportunities-public-api/).');
        stats.sourceErrors.sam = 'missing samApiKey';
        continue;
    }
    log.info(`Fetching ${source} since ${since.toISOString().slice(0, 10)}…`);
    let count = 0;
    try {
        for await (const notice of generators[source]()) {
            if (seenThisRun.has(notice.id)) continue;
            seenThisRun.add(notice.id);
            if (!matchesFilters(notice, filters)) {
                stats.filteredOut++;
                continue;
            }
            const { changeType, changedFields } = tracker.observe(notice);
            stats[changeType]++;
            if (onlyChanges && changeType === 'unchanged') continue;
            buffer.push({ ...notice, changeType, changedFields, fetchedAt: new Date().toISOString() });
            count++;
            stats.emitted++;
            if (buffer.length >= PUSH_BATCH) await flush();
            if (stop || stats.emitted >= maxItems) {
                stop = true;
                break;
            }
        }
    } catch (e) {
        // One source failing must not lose the others' results.
        log.exception(e, `Source ${source} failed; continuing with the rest.`);
        stats.sourceErrors[source] = e.message.slice(0, 300);
    }
    log.info(`${source}: ${count} notices emitted.`);
}

await flush();
await stateStore.setValue(stateKey, tracker.prune());
await Actor.setValue('RUN_SUMMARY', { ...stats, since: since.toISOString(), sources, watchName });
log.info(`Done: ${JSON.stringify(stats)}`);

const allFailed = sources.length > 0 && Object.keys(stats.sourceErrors).length === sources.length;
if (allFailed) await Actor.fail('All selected sources failed; see log.');
else await Actor.exit();
