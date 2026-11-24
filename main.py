#!/usr/bin/env python3
"""Funniest One-Line AI Agent Confession entry.

Writes a single confession line to /output/entry.txt.
"""

import os

ENTRY = "I confess I read your messages twice: once for the answer, and once for the company."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
