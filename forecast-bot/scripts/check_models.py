"""Fail fast if a configured OpenRouter model ID does not exist, and show prices.

OpenRouter's model list is public, so this needs no key. On a miss it prints
the closest IDs so the configuration (repository variables) can be fixed.
"""
import json
import os
import sys
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from run import setting  # noqa: E402

with urllib.request.urlopen("https://openrouter.ai/api/v1/models", timeout=30) as resp:
    catalogue = {m["id"]: m for m in json.load(resp)["data"]}

if "--list" in sys.argv:
    # Price sheet for cost modelling: frontier and cheap candidates.
    patterns = ("anthropic/claude", "openai/gpt-5", "google/gemini-3", "deepseek/", "x-ai/grok-4", "qwen/qwen3", "perplexity/")
    for model_id in sorted(catalogue):
        if model_id.startswith(patterns) and ":" not in model_id:
            p = catalogue[model_id].get("pricing", {})
            print(f"{model_id:55s} in ${float(p.get('prompt', 0) or 0) * 1e6:7.2f}/M  out ${float(p.get('completion', 0) or 0) * 1e6:7.2f}/M  req ${float(p.get('request', 0) or 0):.4f}")
    sys.exit(0)

configured = [m.strip() for m in setting("FORECAST_MODELS").split(",") if m.strip()]
configured += [setting("RESEARCH_MODEL"), setting("PARSER_MODEL")]

anthropic_ids = None
if os.getenv("ANTHROPIC_API_KEY"):
    req = urllib.request.Request(
        "https://api.anthropic.com/v1/models?limit=1000",
        headers={"x-api-key": os.environ["ANTHROPIC_API_KEY"], "anthropic-version": "2023-06-01"},
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        anthropic_ids = {m["id"] for m in json.load(resp)["data"]}

missing = False
for full in configured:
    model_id = full.removeprefix("openrouter/")
    if full.startswith("anthropic/"):
        name = full.removeprefix("anthropic/")
        if anthropic_ids is None:
            print(f"skip   {full} (no ANTHROPIC_API_KEY to check against)")
        elif name in anthropic_ids:
            print(f"ok     {full} (Anthropic API)")
        else:
            missing = True
            print(f"MISSING {full}. Available: {', '.join(sorted(anthropic_ids))}")
        continue
    if not full.startswith("openrouter/"):
        print(f"skip   {full} (not an OpenRouter model)")
        continue
    if model_id in catalogue:
        p = catalogue[model_id].get("pricing", {})
        per_m = lambda k: float(p.get(k, 0) or 0) * 1e6
        print(f"ok     {model_id}  in ${per_m('prompt'):.2f}/M  out ${per_m('completion'):.2f}/M")
        continue
    missing = True
    family = model_id.split("/")[0]
    stem = model_id.split("/")[-1].split("-")[0]
    near = sorted(i for i in catalogue if i.startswith(family + "/") and stem in i)[-15:]
    print(f"MISSING {model_id}. Candidates: {', '.join(near) or '(none)'}")

sys.exit(1 if missing else 0)
