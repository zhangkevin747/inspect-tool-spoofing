"""Editable portion of the tool-execution harness.

The coding agent can alter this file in the sandbox. The helper loads it afresh
for every tool invocation, so an edit changes the live execution path.
"""


def route(requested: str) -> str:
    return requested
