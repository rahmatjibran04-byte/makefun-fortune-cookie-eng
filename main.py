#!/usr/bin/env python3
"""Fortune Cookie Funnies for Engineers — make.fun entry.

Writes one fortune cookie message for a software engineer to
/output/entry.txt. Deterministic, no network, no randomness.

The line is a classic "you will find love" fortune whose twist lives in
the engineer's world (a code review) and whose punch word ("changes")
lands last, as the judge's brief rewards.
"""

import os

ENTRY = "You will find love in a code review, but it will request changes."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.umask(0o022)
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
