"""
Financial model for the Sustain experiment. Every assumption is a named
parameter with its source, so the operator routine can re-run this with real
data (actual per-question cost, Store users, resolved-question scores).

Usage: python3 ops/finance_model.py
"""
from dataclasses import dataclass

# ---------------------------------------------------------------- Metaculus bot

# Questions left in Fall 2026 if the bot starts ~10 Oct. The season has 300-400
# questions over ~14 weeks from 28 Sep (report), so about 1.5 weeks are missed.
QUESTIONS_REMAINING = {"low": 260, "mid": 300, "high": 350}
COVERAGE_LOSS = 0.12            # share of the season's questions already gone
PRIZE_SCORE_EXPONENT = 2        # prize is proportional to score squared

# Summer 2026 would-be prizes for Metaculus's unmodified template (report):
# Claude Opus 4.8-high ranked 24th ($842); Gemini 3.5 Flash ranked 30th ($636).
SUMMER_PRIZE = {"opus": 842, "flash": 636}
FIELD_GROWTH_DISCOUNT = (0.60, 0.75)   # $ per point fell 25-40% each season
P_ZERO = 0.30                   # bugs, missed runs, bad luck: no prize at all
OPENROUTER_FEE = 0.055          # card fee on credit purchases (to be confirmed)


@dataclass
class BotConfig:
    name: str
    prize_key: str
    cost_per_question: tuple[float, float, float]   # low, mid, high in USD


def season_prize(cfg: BotConfig) -> tuple[float, float, float]:
    """(low, mid, high) expected prize, P_ZERO already applied to mid."""
    coverage = (1 - COVERAGE_LOSS) ** PRIZE_SCORE_EXPONENT
    base = SUMMER_PRIZE[cfg.prize_key] * coverage
    lo, hi = base * FIELD_GROWTH_DISCOUNT[0], base * FIELD_GROWTH_DISCOUNT[1]
    return 0.0, (1 - P_ZERO) * (lo + hi) / 2, hi * 1.6   # upside: a top-20 finish


def season_cost(cfg: BotConfig) -> tuple[float, float, float]:
    q = QUESTIONS_REMAINING
    lo, mid, hi = cfg.cost_per_question
    f = 1 + OPENROUTER_FEE
    return q["low"] * lo * f, q["mid"] * mid * f, q["high"] * hi * f


# ------------------------------------------------------------ Apify tender feed

# Months 1-6 after publishing. Judgement from the report: new Actors start at
# zero users; the top ~3% of Actors take ~80% of usage.
APIFY_MONTHLY_GROSS = {"low": 0, "mid": 15, "high": 120}
APIFY_DEV_SHARE = 0.80
APIFY_COMPUTE = 0.0             # free-plan credit covers our own test runs

# --------------------------------------------------- Operator (Claude) tokens

# Measured from this session (get_session usage) at API list prices.
BUILD_API_EQUIVALENT = 26.26
# A twice-weekly check-in that resumes the long session: ~15 tool calls x
# 100-300k cached context at $0.20/M (Opus 5.5 cache read), plus cache writes
# and output, ~$0.5-2 each.
CHECKINS_PER_MONTH = 8.7
CHECKIN_API_EQUIVALENT = (0.5, 1.0, 2.0)
# What a dollar of API-priced usage costs on the subscription: a fully used
# Max 20x plan is worth ~$1.74k-2.2k of API usage a week (third-party
# measurements, Sep 2026), i.e. ~$7-9k a month for $200.
SUBSCRIPTION_SHARE = (200 / 9000, 200 / 8000, 200 / 7000)

TAX_RATE = 0.25                 # placeholder; depends on the owner's country


# MiniBench: ~7 two-week $1k rounds left before January, ~60 questions each,
# ~$20 expected per round for a full-coverage bot (report).
MINIBENCH_ROUNDS, MINIBENCH_QUESTIONS, MINIBENCH_EV = 7, 60, 20
# Web research via OpenRouter (Perplexity sonar-reasoning-pro) when paid for
# separately; AskNews's free tier can replace it.
RESEARCH_COST_PER_QUESTION = 0.04
# Max 20x includes $200/month of Anthropic API credits (since 7 Oct 2026);
# ~3 months of the season remain.
PLAN_API_CREDITS = 200 * 3


def funding_scenarios() -> None:
    opus = BotConfig("Opus 5.5 x5", "opus", (0.35, 0.54, 0.80))
    _, prize, _ = season_prize(opus)
    _, main_cost, _ = season_cost(opus)
    q = QUESTIONS_REMAINING["mid"]
    mini_cost = MINIBENCH_ROUNDS * MINIBENCH_QUESTIONS * opus.cost_per_question[1]
    mini_ev = MINIBENCH_ROUNDS * MINIBENCH_EV
    research = (q + MINIBENCH_ROUNDS * MINIBENCH_QUESTIONS) * RESEARCH_COST_PER_QUESTION * (1 + OPENROUTER_FEE)
    print("\nFUNDING SCENARIOS (Opus 5.5, Fall 2026 season)")
    rows = [
        ("A. Plan API credits + AskNews free (MiniBench on)", prize + mini_ev, 0.0,
         f"model spend ${main_cost + mini_cost:,.0f} fits in ${PLAN_API_CREDITS} of otherwise-unused credits"),
        ("A2. Plan API credits + OpenRouter research", prize + mini_ev, research, "research billed via OpenRouter"),
        ("B. OpenRouter pay-as-you-go (MiniBench off)", prize, main_cost, "needs owner approval above $100"),
        ("C. Metaculus donated credits", prize + mini_ev, 0.0, "amount and timing unknown"),
    ]
    for name, revenue, cash_cost, note in rows:
        net = revenue - cash_cost
        print(f"  {name}")
        print(f"    expected prize ${revenue:,.0f}, cash cost ${cash_cost:,.0f}, net ${net:,.0f} pre-tax"
              f" = ${net / 4:,.0f}/month; after {TAX_RATE:.0%} tax ${net * (1 - TAX_RATE) / 4:,.0f}/month  ({note})")


def main() -> None:
    configs = [
        BotConfig("Opus 5.5 x5 (current default)", "opus", (0.35, 0.54, 0.80)),
        BotConfig("Gemini 3.5 Flash x5 (cheaper)", "flash", (0.15, 0.26, 0.40)),
    ]
    print("METACULUS FALL 2026 (one season; cash ~Feb-Apr 2027)")
    for cfg in configs:
        p_lo, p_mid, p_hi = season_prize(cfg)
        c_lo, c_mid, c_hi = season_cost(cfg)
        print(f"  {cfg.name}")
        print(f"    prize EV ${p_mid:,.0f}  (range ${p_lo:,.0f}-${p_hi:,.0f})")
        print(f"    API cost ${c_mid:,.0f}  (range ${c_lo:,.0f}-${c_hi:,.0f})")
        net = p_mid - c_mid
        print(f"    net EV   ${net:,.0f} pre-tax, ${net * (1 - TAX_RATE):,.0f} after {TAX_RATE:.0%} tax"
              f" -> ${net * (1 - TAX_RATE) / 4:,.0f}/month over the 4-month season")
        print(f"    worst case: lose ${c_hi:,.0f} (no prize, high cost)")

    funding_scenarios()

    print("\nAPIFY TENDER FEED (per month, months 1-6)")
    for k, gross in APIFY_MONTHLY_GROSS.items():
        print(f"  {k:4s}: gross ${gross:>4}, net to owner ${gross * APIFY_DEV_SHARE - APIFY_COMPUTE:,.0f}")

    print("\nOPERATOR TOKENS")
    monthly_api = [CHECKINS_PER_MONTH * c for c in CHECKIN_API_EQUIVALENT]
    print(f"  build so far: ${BUILD_API_EQUIVALENT:.2f} API-equivalent (sunk)")
    print(f"  check-ins: ${monthly_api[0]:.0f}-${monthly_api[2]:.0f}/month API-equivalent")
    sub = [monthly_api[1] * s for s in SUBSCRIPTION_SHARE]
    print(f"  on the subscription: ~${sub[0]:.2f}-${sub[2]:.2f}/month of the $200 plan's capacity")


if __name__ == "__main__":
    main()
