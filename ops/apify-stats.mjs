#!/usr/bin/env node
// Print Store stats and recent run health for each of our Actors, for the
// ledger. Usage: APIFY_TOKEN=... node ops/apify-stats.mjs
const token = process.env.APIFY_TOKEN;
if (!token) {
    console.error('APIFY_TOKEN not set');
    process.exit(2);
}
async function api(path) {
    const res = await fetch(`https://api.apify.com/v2${path}`, { headers: { authorization: `Bearer ${token}` } });
    if (!res.ok) throw new Error(`${path} -> ${res.status}: ${(await res.text()).slice(0, 300)}`);
    return (await res.json()).data;
}
const me = await api('/users/me');
const acts = await api('/acts?my=true&limit=100');
for (const a of acts.items) {
    const actor = await api(`/acts/${a.id}`);
    const runs = await api(`/acts/${a.id}/runs?desc=1&limit=100`);
    const byStatus = runs.items.reduce((m, r) => ({ ...m, [r.status]: (m[r.status] ?? 0) + 1 }), {});
    console.log(JSON.stringify({
        actor: `${me.username}/${actor.name}`,
        isPublic: actor.isPublic,
        stats: actor.stats,
        pricing: actor.pricingInfos?.at(-1)?.pricingModel ?? null,
        last100RunsByStatus: byStatus,
    }, null, 2));
}
