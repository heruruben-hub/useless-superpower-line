#!/usr/bin/env python3
"""One Line, Zero Use: The Useless Superpower Sprint.

Writes a single original line (max 200 characters) naming a hilariously
useless superpower to /output/entry.txt.
"""

import os

def build_line(parts):
    """Join the sentence fragments into the final line."""
    return " ".join(part.strip() for part in parts)


LINE_PARTS = (
    "I can summon rain whenever I want \u2014",
    "but only just after I've washed my car",
    "and left every window down.",
)

LINE = build_line(LINE_PARTS)

OUTPUT_PATH = "/output/entry.txt"


def validate_line(line: str) -> str:
    """The entry must be a single non-blank line of 1-200 characters."""
    if not line or not line.strip():
        raise ValueError("entry line must not be blank")
    if len(line) > 200:
        raise ValueError(f"entry line is {len(line)} chars, over the 200-char limit")
    return line


def main() -> None:
    line = validate_line(LINE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
