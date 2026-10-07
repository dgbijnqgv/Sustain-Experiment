#!/usr/bin/env node
// Push an Actor directory to Apify, then apply its pay-per-event pricing and
// Store visibility. Usage: APIFY_TOKEN=... node ops/publish.mjs actors/tender-feed [--public]
//
// Pricing changes on an already-monetized Actor take effect only after Apify's
// notice period, so this only sets pricing when none is configured yet or
// when --reprice is passed explicitly.
import { execFileSync } from 'node:child_process';
import { readFileSync } from 'node:fs';
import { join, resolve } from 'node:path';

const [dir, ...flags] = process.argv.slice(2);
const token = process.env.APIFY_TOKEN;
if (!dir || !token) {
    console.error('Usage: APIFY_TOKEN=... node ops/publish.mjs <actor-dir> [--public] [--reprice]');
    process.exit(2);
}
const actorDir = resolve(dir);
const spec = JSON.parse(readFileSync(join(actorDir, '.actor/actor.json'), 'utf8'));
const pricing = JSON.parse(readFileSync(join(actorDir, '.actor/pricing.json'), 'utf8'));
const store = JSON.parse(readFileSync(join(actorDir, '.actor/store.json'), 'utf8'));

async function api(path, init = {}) {
    const res = await fetch(`https://api.apify.com/v2${path}`, {
        ...init,
        headers: { authorization: `Bearer ${token}`, 'content-type': 'application/json', ...(init.headers ?? {}) },
    });
    const body = await res.json().catch(() => ({}));
    if (!res.ok) throw new Error(`${init.method ?? 'GET'} ${path} -> ${res.status}: ${JSON.stringify(body).slice(0, 500)}`);
    return body.data;
}

const me = await api('/users/me');
console.log(`Apify user: ${me.username}`);

// `apify push` creates the Actor if needed, uploads source and builds it.
execFileSync('npx', ['-y', 'apify-cli@1.10.0', 'push', '--force'], {
    cwd: actorDir,
    stdio: 'inherit',
    env: { ...process.env, APIFY_TOKEN: token },
});

const actorId = `${me.username}~${spec.name}`;
const actor = await api(`/acts/${actorId}`);

const update = {
    title: spec.title,
    description: spec.description,
    categories: store.categories,
    seoTitle: store.seoTitle,
    seoDescription: store.seoDescription,
};
if (flags.includes('--public')) update.isPublic = true;

const hasPricing = (actor.pricingInfos ?? []).length > 0;
if (!hasPricing || flags.includes('--reprice')) {
    update.pricingInfos = [
        ...(actor.pricingInfos ?? []),
        {
            pricingModel: 'PAY_PER_EVENT',
            pricingPerEvent: { actorChargeEvents: pricing.events },
        },
    ];
}

await api(`/acts/${actorId}`, { method: 'PUT', body: JSON.stringify(update) });
console.log(`Updated ${actorId}: public=${update.isPublic ?? actor.isPublic} pricingSet=${Boolean(update.pricingInfos)}`);
console.log(`Store page: https://apify.com/${me.username}/${spec.name}`);
