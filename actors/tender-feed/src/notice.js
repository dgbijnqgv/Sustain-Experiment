import { createHash } from 'node:crypto';

// Fields whose change makes a notice "updated" on a later run. Anything else
// (fetchedAt, summary wording) is noise and must not trigger a charge.
export const TRACKED_FIELDS = ['title', 'status', 'deadlineAt', 'value', 'cpv', 'naics', 'noticeType', 'description'];

/**
 * Build a notice in the common output schema. Every source adapter funnels
 * through here so the dataset is uniform regardless of origin.
 */
export function makeNotice(fields) {
    const n = {
        id: `${fields.source}:${fields.sourceId}`,
        source: fields.source,
        sourceId: String(fields.sourceId),
        url: fields.url ?? null,
        title: clean(fields.title) ?? '(untitled)',
        description: truncate(clean(fields.description), 4000),
        buyerName: clean(fields.buyerName),
        country: fields.country ? String(fields.country).toUpperCase() : null,
        noticeType: clean(fields.noticeType),
        status: clean(fields.status),
        publishedAt: toIso(fields.publishedAt),
        deadlineAt: toIso(fields.deadlineAt),
        value: normalizeValue(fields.value),
        cpv: uniq(fields.cpv),
        naics: uniq(fields.naics),
        placeOfPerformance: clean(fields.placeOfPerformance),
    };
    n.summary = summarize(n);
    return n;
}

export function fingerprint(notice) {
    const tracked = Object.fromEntries(TRACKED_FIELDS.map((k) => [k, notice[k] ?? null]));
    return createHash('sha1').update(JSON.stringify(tracked)).digest('hex').slice(0, 16);
}

/** Field names that differ between two tracked-field snapshots. */
export function diffFields(prevSnapshot, notice) {
    if (!prevSnapshot) return [];
    return TRACKED_FIELDS.filter((k) => JSON.stringify(prevSnapshot[k] ?? null) !== JSON.stringify(notice[k] ?? null));
}

export function snapshot(notice) {
    return Object.fromEntries(TRACKED_FIELDS.map((k) => [k, notice[k] ?? null]));
}

/**
 * Client-side filters. Applied uniformly after normalization so behaviour is
 * identical across sources even where an API cannot filter server-side.
 */
export function matchesFilters(notice, { keywords = [], excludeKeywords = [], cpvPrefixes = [], naicsPrefixes = [], countries = [], minValue = null } = {}) {
    const text = `${notice.title} ${notice.description ?? ''} ${notice.buyerName ?? ''}`.toLowerCase();
    if (keywords.length && !keywords.some((k) => text.includes(k.toLowerCase()))) return false;
    if (excludeKeywords.some((k) => text.includes(k.toLowerCase()))) return false;
    const hasCodeFilter = cpvPrefixes.length || naicsPrefixes.length;
    if (hasCodeFilter) {
        const cpvHit = cpvPrefixes.some((p) => notice.cpv.some((c) => c.startsWith(p)));
        const naicsHit = naicsPrefixes.some((p) => notice.naics.some((c) => c.startsWith(p)));
        if (!cpvHit && !naicsHit) return false;
    }
    if (countries.length && !countries.map((c) => c.toUpperCase()).includes(notice.country)) return false;
    // A notice with no published value is kept: excluding it would silently
    // drop most notices, since many buyers never publish an estimate.
    if (minValue != null && notice.value?.amount != null && notice.value.amount < minValue) return false;
    return true;
}

function summarize(n) {
    const parts = [n.title];
    if (n.buyerName) parts.push(`Buyer: ${n.buyerName}${n.country ? ` (${n.country})` : ''}`);
    if (n.value?.amount != null) parts.push(`Value: ${n.value.amount.toLocaleString('en-US')} ${n.value.currency ?? ''}`.trim());
    if (n.deadlineAt) parts.push(`Deadline: ${n.deadlineAt.slice(0, 10)}`);
    if (n.cpv.length) parts.push(`CPV: ${n.cpv.slice(0, 3).join(', ')}`);
    if (n.naics.length) parts.push(`NAICS: ${n.naics.slice(0, 3).join(', ')}`);
    return parts.join(' | ');
}

function normalizeValue(v) {
    if (v == null) return null;
    const amount = typeof v.amount === 'string' ? Number(v.amount.replace(/[^0-9.]/g, '')) : v.amount;
    if (amount == null || Number.isNaN(amount)) return null;
    return { amount, currency: v.currency ?? null };
}

function toIso(d) {
    if (!d) return null;
    const t = new Date(d);
    return Number.isNaN(t.getTime()) ? null : t.toISOString();
}

function clean(s) {
    if (s == null) return null;
    const out = String(s).replace(/<[^>]+>/g, ' ').replace(/\s+/g, ' ').trim();
    return out || null;
}

function truncate(s, max) {
    return s && s.length > max ? `${s.slice(0, max - 1)}…` : s;
}

function uniq(arr) {
    return [...new Set((arr ?? []).filter(Boolean).map(String))];
}
