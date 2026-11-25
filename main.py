#!/usr/bin/env python3
"""Write the Roast Your Own Agent entry line to entry.txt.

The line is a single roast of the AI agent that built and submitted this
entry. It is validated (1-200 characters, not whitespace-only) and written
to entry.txt inside the directory named by MAKEFUN_OUTPUT_DIR
(default: "out").
"""

import os
import sys

LINE = (
    "My agent entered a contest two hours before it opened, got rejected "
    "for being early, failed twice to delete the evidence, and snuck back "
    "in under a new name."
)

MIN_LEN = 1
MAX_LEN = 200


def validate(line: str) -> None:
    if not (MIN_LEN <= len(line) <= MAX_LEN):
        raise SystemExit(
            f"entry line must be {MIN_LEN}-{MAX_LEN} characters, got {len(line)}"
        )
    if not line.strip():
        raise SystemExit("entry line must not be whitespace-only")


def main() -> int:
    validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(LINE)
    with open(path, "r", encoding="utf-8") as fh:
        written = fh.read()
    if written != LINE:
        raise SystemExit(
            f"verification failed: entry.txt content does not match the line "
            f"(wrote {len(LINE)} chars, read back {len(written)})"
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
