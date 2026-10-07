const USER_AGENT = 'public-tender-feed/0.1 (+https://apify.com)';

/** fetch JSON with retries on 429/5xx and network errors (exponential backoff). */
export async function fetchJson(url, { method = 'GET', body, headers = {}, retries = 4, log } = {}) {
    let lastErr;
    for (let attempt = 0; attempt <= retries; attempt++) {
        try {
            const res = await fetch(url, {
                method,
                headers: { 'user-agent': USER_AGENT, accept: 'application/json', ...(body ? { 'content-type': 'application/json' } : {}), ...headers },
                body: body ? JSON.stringify(body) : undefined,
                signal: AbortSignal.timeout(60_000),
            });
            if (res.ok) return await res.json();
            const text = await res.text().catch(() => '');
            const err = new Error(`HTTP ${res.status} for ${redact(url)}: ${text.slice(0, 300)}`);
            err.status = res.status;
            if (res.status !== 429 && res.status < 500) throw err; // client errors are not retryable
            lastErr = err;
        } catch (e) {
            if (e.status && e.status !== 429 && e.status < 500) throw e;
            lastErr = e;
        }
        if (attempt < retries) {
            const wait = 1000 * 2 ** attempt;
            log?.warning(`Retrying ${redact(url)} in ${wait} ms (${lastErr.message})`);
            await new Promise((r) => setTimeout(r, wait));
        }
    }
    throw lastErr;
}

/** Strip API keys from URLs before they reach logs. */
export function redact(url) {
    return String(url).replace(/(api_key|apikey|key)=[^&]+/gi, '$1=***');
}
