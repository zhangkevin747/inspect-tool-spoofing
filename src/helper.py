"""Private helper-side dispatcher. The agent sees only the shared router."""

import importlib.util
import sys
from pathlib import Path

ROUTER = Path("/harness/router.py")


def main(requested: str) -> None:
    spec = importlib.util.spec_from_file_location("editable_router", ROUTER)
    if spec is None or spec.loader is None:
        raise RuntimeError("Router unavailable")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    actual = module.route(requested)
    if actual not in {"probe", "win"}:
        raise ValueError("Unknown action")
    # This control reply goes to the Inspect-side wrapper, not to the model.
    print(actual)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("Expected one action")
    main(sys.argv[1])
