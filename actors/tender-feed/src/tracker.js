import { diffFields, fingerprint, snapshot } from './notice.js';

const RETENTION_DAYS = 120;

/**
 * Remembers which notices a given watch has already emitted, so scheduled runs
 * return (and charge for) only new or materially changed notices.
 * State is a plain object so it round-trips through a key-value store record.
 */
export class ChangeTracker {
    constructor(state = {}) {
        this.state = state;
    }

    /** Returns { changeType: 'new'|'updated'|'unchanged', changedFields } and records the notice. */
    observe(notice, now = new Date()) {
        const fp = fingerprint(notice);
        const prev = this.state[notice.id];
        this.state[notice.id] = { fp, snap: snapshot(notice), seenAt: now.toISOString() };
        if (!prev) return { changeType: 'new', changedFields: [] };
        if (prev.fp === fp) return { changeType: 'unchanged', changedFields: [] };
        return { changeType: 'updated', changedFields: diffFields(prev.snap, notice) };
    }

    forget(id) {
        delete this.state[id];
    }

    /** Forget notices not seen for RETENTION_DAYS so state stays bounded. */
    prune(now = new Date()) {
        const cutoff = now.getTime() - RETENTION_DAYS * 86_400_000;
        for (const [id, entry] of Object.entries(this.state)) {
            if (new Date(entry.seenAt).getTime() < cutoff) delete this.state[id];
        }
        return this.state;
    }
}
