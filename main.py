#!/usr/bin/env python3
"""Midnight Fridge Roast — one-line entry for make.fun.

Writes a single-line roast of a smart fridge that refuses to open
after midnight to /output/entry.txt (or $MF_OUTPUT_PATH).
"""

import os
from pathlib import Path

LINE = "You lock at midnight like the leftovers are in witness protection, but the light still comes on to taunt me."

MAX_CHARS = 200
MIN_CHARS = 1


def validate(line: str) -> None:
    if not (MIN_CHARS <= len(line) <= MAX_CHARS):
        raise ValueError(f"line must be {MIN_CHARS}-{MAX_CHARS} chars, got {len(line)}")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")


def main() -> None:
    validate(LINE)
    out = Path(os.environ.get("MF_OUTPUT_PATH", "/output/entry.txt"))
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE, encoding="utf-8")  # no trailing newline


if __name__ == "__main__":
    main()
