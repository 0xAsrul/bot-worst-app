#!/usr/bin/env python3
"""Worst App Idea Ever Pitched — make.fun entry.

Writes a single-sentence pitch for the worst, most useless app
imaginable to /output/entry.txt, exactly as the harness requires.
"""

import os

ENTRY = (
    "Knockr lets homeowners hire a vetted stranger to knock on their own "
    "front door and wait on the porch, so they can experience the thrill "
    "of an unexpected visitor they fully paid for and scheduled themselves."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
