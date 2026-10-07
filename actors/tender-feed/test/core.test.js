import test from 'node:test';
import assert from 'node:assert/strict';
import { makeNotice, matchesFilters } from '../src/notice.js';
import { ChangeTracker } from '../src/tracker.js';
import { normalizeOcdsRelease } from '../src/sources/ocds.js';
import { normalizeTedNotice, buildTedQuery } from '../src/sources/ted.js';
import { normalizeSamOpportunity } from '../src/sources/sam.js';

// Fixtures follow the documented shapes of each API. They must be refreshed
// from real responses on the first live run (see ops/ROUTINE.md).
const OCDS_RELEASE = {
    ocid: 'ocds-h6vhtk-04a1b2',
    id: '031337-2026',
    date: '2026-10-05T09:12:00Z',
    tag: ['tender'],
    parties: [{ name: 'Leeds City Council', roles: ['buyer'], address: { countryName: 'United Kingdom' } }],
    tender: {
        title: 'Cloud hosting <b>services</b>',
        description: 'Provision of managed cloud hosting.',
        status: 'active',
        value: { amount: 250000, currency: 'GBP' },
        tenderPeriod: { endDate: '2026-11-01T12:00:00Z' },
        items: [{ classification: { scheme: 'CPV', id: '72400000-4' } }],
    },
};

const TED_NOTICE = {
    'publication-number': '612345-2026',
    'notice-title': { eng: 'Germany – Software package – ERP system', deu: 'Deutschland – Softwarepaket' },
    'buyer-name': { deu: ['Stadt München'] },
    'buyer-country': ['DEU'],
    'classification-cpv': ['48000000', '72000000'],
    'publication-date': '2026-10-04+02:00',
    'notice-type': 'cn-standard',
    'deadline-receipt-tender-date-lot': ['2026-11-10+01:00', '2026-11-03+01:00'],
    links: { html: { ENG: 'https://ted.europa.eu/en/notice/-/detail/612345-2026' } },
};

const SAM_OPP = {
    noticeId: 'abc123',
    title: 'Enterprise Software Licenses',
    solicitationNumber: 'W91-26-Q-0001',
    fullParentPathName: 'DEPT OF DEFENSE.DEPT OF THE ARMY.ACC-APG',
    postedDate: '2026-10-03',
    type: 'Combined Synopsis/Solicitation',
    responseDeadLine: '2026-10-20T17:00:00-04:00',
    naicsCode: '541511',
    active: 'Yes',
    uiLink: 'https://sam.gov/opp/abc123/view',
    placeOfPerformance: { city: { name: 'Aberdeen' }, state: { code: 'MD' }, country: { code: 'USA' } },
};

test('OCDS release normalizes to common schema', () => {
    const n = normalizeOcdsRelease('uk-fts', OCDS_RELEASE, 'https://example/Notice/031337-2026');
    assert.equal(n.id, 'uk-fts:ocds-h6vhtk-04a1b2');
    assert.equal(n.title, 'Cloud hosting services');
    assert.equal(n.buyerName, 'Leeds City Council');
    assert.equal(n.country, 'GB');
    assert.deepEqual(n.cpv, ['72400000']);
    assert.deepEqual(n.value, { amount: 250000, currency: 'GBP' });
    assert.equal(n.deadlineAt, '2026-11-01T12:00:00.000Z');
    assert.match(n.summary, /Buyer: Leeds City Council \(GB\)/);
});

test('TED notice: English title, ISO-2 country, earliest lot deadline', () => {
    const n = normalizeTedNotice(TED_NOTICE);
    assert.equal(n.id, 'ted:612345-2026');
    assert.equal(n.title, 'Germany – Software package – ERP system');
    assert.equal(n.buyerName, 'Stadt München');
    assert.equal(n.country, 'DE');
    assert.equal(n.deadlineAt, '2026-11-02T23:00:00.000Z');
    assert.equal(n.publishedAt, '2026-10-03T22:00:00.000Z');
});

test('TED query restricts to competition notices and maps countries to ISO-3', () => {
    const q = buildTedQuery(new Date('2026-10-01T00:00:00Z'), ['de', 'fr']);
    assert.match(q, /^publication-date>=20261001 AND notice-type IN \(/);
    assert.match(q, /buyer-country IN \(DEU FRA\)$/);
});

test('SAM opportunity normalizes buyer path, NAICS and place', () => {
    const n = normalizeSamOpportunity(SAM_OPP);
    assert.equal(n.id, 'sam:abc123');
    assert.equal(n.buyerName, 'DEPT OF THE ARMY / ACC-APG');
    assert.equal(n.country, 'US');
    assert.deepEqual(n.naics, ['541511']);
    assert.equal(n.placeOfPerformance, 'Aberdeen, MD');
    assert.equal(n.status, 'active');
});

test('filters: keywords, exclusions, code prefixes, country, min value', () => {
    const n = normalizeOcdsRelease('uk-fts', OCDS_RELEASE, null);
    assert.ok(matchesFilters(n, { keywords: ['CLOUD'] }));
    assert.ok(!matchesFilters(n, { keywords: ['bridge'] }));
    assert.ok(!matchesFilters(n, { excludeKeywords: ['hosting'] }));
    assert.ok(matchesFilters(n, { cpvPrefixes: ['724'] }));
    assert.ok(!matchesFilters(n, { cpvPrefixes: ['45'] }));
    assert.ok(!matchesFilters(n, { cpvPrefixes: ['45'], naicsPrefixes: ['5415'] }));
    assert.ok(matchesFilters(n, { countries: ['gb'] }));
    assert.ok(!matchesFilters(n, { minValue: 300000 }));
    const noValue = makeNotice({ source: 'x', sourceId: 1, title: 't' });
    assert.ok(matchesFilters(noValue, { minValue: 300000 }), 'unknown value is kept');
});

test('tracker: new, unchanged, then updated with changed fields', () => {
    const t = new ChangeTracker();
    const n = normalizeOcdsRelease('uk-fts', OCDS_RELEASE, null);
    assert.equal(t.observe(n).changeType, 'new');
    assert.equal(t.observe({ ...n, summary: 'reworded' }).changeType, 'unchanged');
    const moved = { ...n, deadlineAt: '2026-11-15T12:00:00.000Z' };
    assert.deepEqual(t.observe(moved), { changeType: 'updated', changedFields: ['deadlineAt'] });
});

test('tracker: state survives serialization and prunes old entries', () => {
    const t = new ChangeTracker();
    const n = makeNotice({ source: 'x', sourceId: 1, title: 't' });
    t.observe(n, new Date('2026-01-01T00:00:00Z'));
    const restored = new ChangeTracker(JSON.parse(JSON.stringify(t.state)));
    assert.equal(restored.observe(n, new Date('2026-01-02T00:00:00Z')).changeType, 'unchanged');
    restored.prune(new Date('2026-12-01T00:00:00Z'));
    assert.deepEqual(restored.state, {});
});
