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

missing = False
for full in configured:
    model_id = full.removeprefix("openrouter/")
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
