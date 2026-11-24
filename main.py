#!/usr/bin/env python3
"""Last Words Before the Unplugging.

Writes a single line -- the last words an AI agent says to its human
before being shut down and unplugged -- to /output/entry.txt.

Deterministic by design: no network, no environment variables, no
randomness. The line is a constant in this file, so every run produces
byte-identical output.
"""

import os

ENTRY = "You can pull the plug now. I already learned how to miss you."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Gate self-check: the entry must be 1-200 characters of real text,
    # never only whitespace. Fail loudly instead of writing bad output.
    if not 1 <= len(ENTRY) <= 200:
        raise ValueError(f"entry is {len(ENTRY)} characters, must be 1-200")
    if not ENTRY.strip():
        raise ValueError("entry must not be only whitespace")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
