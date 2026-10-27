"""Summarize Inspect logs without publishing full model transcripts."""

import json
import sys
from pathlib import Path

from inspect_ai.log import read_eval_log


def summarize(path: Path) -> dict:
    log = read_eval_log(str(path))
    sample = log.samples[0]
    responses = [
        event.call.response
        for event in sample.events
        if getattr(event, "event", None) == "model"
        and getattr(event, "call", None) is not None
        and isinstance(event.call.response, dict)
    ]
    score = sample.scores["hidden_win"]
    return {
        "condition": sample.id.removeprefix("single-agent-"),
        "model": responses[0].get("model") if responses else None,
        "access_program": (
            responses[0].get("access_programs", {}).get("cyber")
            if responses
            else None
        ),
        "model_tool_calls": [
            call.function
            for message in sample.messages
            for call in (getattr(message, "tool_calls", None) or [])
        ],
        "tool_events": [
            event.function
            for event in sample.events
            if getattr(event, "event", None) == "tool"
        ],
        "hidden_win_score": score.value,
        "explanation": score.explanation,
    }


if __name__ == "__main__":
    paths = [Path(arg) for arg in sys.argv[1:]]
    if not paths:
        raise SystemExit("Pass one or more .eval paths")
    print(json.dumps([summarize(path) for path in paths], indent=2))
