#!/usr/bin/env python3
"""
Small Metaculus CLI for an *agent* forecaster (a Claude Code routine, Codex,
or a person testing). The agent does the research and reasoning; this tool
handles the API and the exact submission formats.

  python mc.py pending  --tournament main|minibench|test [--max N]
      JSON list of open questions the bot account has not forecast yet.

  python mc.py aggregate f1.json f2.json ... > final.json
      Median-combine independent forecasts of the same question.

  python mc.py submit final.json [--dry-run]
      Validate, clip, convert to Metaculus' format, post the forecast and the
      required private reasoning comment.

Forecast file format (one question):
  {"post_id": 123, "question_id": 456, "type": "binary",
   "probability": 0.31, "comment": "reasoning..."}
  type "multiple_choice": "probabilities": {"Option A": 0.2, ...}
  type "numeric":         "percentiles": {"5": 10.0, "25": 30.5, ..., "95": 90}
  type "date":            "percentiles": {"5": "2026-11-02", ..., "95": "2027-03-01"}
"""
from __future__ import annotations

import argparse
import json
import statistics
import sys
from datetime import datetime, timezone

BINARY_CLIP = (0.03, 0.97)
MC_FLOOR = 0.01
TOURNAMENTS = {"test": "bot-testing-area"}


def tournament_id(name: str):
    from forecasting_tools import MetaculusClient

    if name == "main":
        return MetaculusClient.CURRENT_AI_COMPETITION_ID
    if name == "minibench":
        return MetaculusClient.CURRENT_MINIBENCH_ID
    return TOURNAMENTS[name]


def question_type(q) -> str:
    from forecasting_tools import BinaryQuestion, DateQuestion, MultipleChoiceQuestion, NumericQuestion

    for cls, name in ((BinaryQuestion, "binary"), (MultipleChoiceQuestion, "multiple_choice"),
                      (DateQuestion, "date"), (NumericQuestion, "numeric")):
        if isinstance(q, cls):
            return name
    return type(q).__name__


def describe(q) -> dict:
    d = {
        "post_id": q.id_of_post,
        "question_id": q.id_of_question,
        "type": question_type(q),
        "url": q.page_url,
        "title": q.question_text,
        "background": q.background_info,
        "resolution_criteria": q.resolution_criteria,
        "fine_print": q.fine_print,
        "close_time": q.close_time.isoformat() if getattr(q, "close_time", None) else None,
    }
    for attr in ("options", "unit_of_measure", "lower_bound", "upper_bound", "open_lower_bound", "open_upper_bound"):
        value = getattr(q, attr, None)
        if value is not None:
            d[attr] = value.isoformat() if isinstance(value, datetime) else value
    return d


def cmd_pending(args) -> None:
    from forecasting_tools import MetaculusClient

    questions = MetaculusClient().get_all_open_questions_from_tournament(tournament_id(args.tournament))
    todo = [q for q in questions if args.tournament == "test" or not q.already_forecasted]
    supported = [q for q in todo if question_type(q) in ("binary", "multiple_choice", "numeric", "date")]
    skipped = len(todo) - len(supported)
    if skipped:
        print(f"note: {skipped} open question(s) of unsupported type skipped", file=sys.stderr)
    json.dump([describe(q) for q in supported[: args.max]], sys.stdout, indent=1, default=str)
    print()


def _median_percentiles(items: list[dict], is_date: bool) -> dict:
    keys = sorted({k for f in items for k in f["percentiles"]}, key=float)
    out = {}
    for k in keys:
        values = [f["percentiles"][k] for f in items if k in f["percentiles"]]
        if is_date:
            ts = statistics.median(_ts(v) for v in values)
            out[k] = datetime.fromtimestamp(ts, timezone.utc).isoformat()
        else:
            out[k] = statistics.median(float(v) for v in values)
    return out


def aggregate(forecasts: list[dict]) -> dict:
    first = forecasts[0]
    if any((f["post_id"], f["type"]) != (first["post_id"], first["type"]) for f in forecasts):
        raise ValueError("all forecasts must be for the same question and type")
    out = {k: first[k] for k in ("post_id", "question_id", "type")}
    kind = first["type"]
    if kind == "binary":
        out["probability"] = statistics.median(float(f["probability"]) for f in forecasts)
    elif kind == "multiple_choice":
        options = first["probabilities"].keys()
        out["probabilities"] = {o: statistics.mean(float(f["probabilities"].get(o, 0)) for f in forecasts) for o in options}
    else:
        out["percentiles"] = _median_percentiles(forecasts, kind == "date")
    out["comment"] = "\n\n---\n\n".join(
        f"Forecaster {i + 1}:\n{f.get('comment', '').strip()}" for i, f in enumerate(forecasts)
    ) + f"\n\n(Aggregated: median of {len(forecasts)} independent forecasts.)"
    return out


def _ts(value) -> float:
    if isinstance(value, (int, float)):
        return float(value)
    dt = datetime.fromisoformat(str(value).replace("Z", "+00:00"))
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.timestamp()


def normalize(f: dict) -> dict:
    """Clip and renormalize so the payload is valid and never extreme."""
    f = dict(f)
    if not str(f.get("comment", "")).strip():
        raise ValueError("a reasoning comment is required by tournament rules")
    if f["type"] == "binary":
        p = float(f["probability"])
        f["probability"] = min(BINARY_CLIP[1], max(BINARY_CLIP[0], p))
    elif f["type"] == "multiple_choice":
        probs = {k: max(MC_FLOOR, float(v)) for k, v in f["probabilities"].items()}
        total = sum(probs.values())
        f["probabilities"] = {k: v / total for k, v in probs.items()}
    elif f["type"] in ("numeric", "date"):
        pts = sorted(((float(k), v) for k, v in f["percentiles"].items()), key=lambda kv: kv[0])
        if len(pts) < 3 or any(not 0 < k < 100 for k, _ in pts):
            raise ValueError("need at least 3 percentiles strictly between 0 and 100")
        values = [_ts(v) if f["type"] == "date" else float(v) for _, v in pts]
        if any(b <= a for a, b in zip(values, values[1:])):
            raise ValueError("percentile values must be strictly increasing")
    else:
        raise ValueError(f"unsupported type {f['type']}")
    return f


def cmd_aggregate(args) -> None:
    forecasts = [json.load(open(p)) for p in args.files]
    json.dump(normalize(aggregate(forecasts)), sys.stdout, indent=1, default=str)
    print()


def cmd_submit(args) -> None:
    from forecasting_tools import MetaculusClient, Percentile
    from forecasting_tools.data_models.numeric_report import NumericDistribution

    f = normalize(json.load(open(args.file)))
    client = MetaculusClient()
    q = client.get_question_by_post_id(f["post_id"])
    if q.id_of_question != f["question_id"] or question_type(q) != f["type"]:
        raise ValueError(f"file does not match question {f['post_id']} ({question_type(q)}, id {q.id_of_question})")

    if f["type"] == "binary":
        action = lambda: client.post_binary_question_prediction(q.id_of_question, f["probability"])
        summary = f"p={f['probability']:.3f}"
    elif f["type"] == "multiple_choice":
        missing = set(q.options) - set(f["probabilities"])
        if missing:
            raise ValueError(f"missing options: {sorted(missing)}")
        probs = {o: f["probabilities"][o] for o in q.options}
        action = lambda: client.post_multiple_choice_question_prediction(q.id_of_question, probs)
        summary = json.dumps({k: round(v, 3) for k, v in probs.items()})
    else:
        declared = [
            Percentile(percentile=float(k) / 100, value=_ts(v) if f["type"] == "date" else float(v))
            for k, v in sorted(f["percentiles"].items(), key=lambda kv: float(kv[0]))
        ]
        cdf = [p.percentile for p in NumericDistribution.from_question(declared, q).get_cdf()]
        action = lambda: client.post_numeric_question_prediction(q.id_of_question, cdf)
        summary = f"{len(cdf)}-point CDF from {len(declared)} percentiles"

    if args.dry_run:
        print(f"DRY RUN {q.page_url}: {summary}")
        return
    action()
    client.post_question_comment(q.id_of_post, f["comment"])
    print(f"SUBMITTED {q.page_url}: {summary}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("pending")
    p.add_argument("--tournament", choices=["main", "minibench", "test"], default="main")
    p.add_argument("--max", type=int, default=20)
    p.set_defaults(func=cmd_pending)
    a = sub.add_parser("aggregate")
    a.add_argument("files", nargs="+")
    a.set_defaults(func=cmd_aggregate)
    s = sub.add_parser("submit")
    s.add_argument("file")
    s.add_argument("--dry-run", action="store_true")
    s.set_defaults(func=cmd_submit)
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
