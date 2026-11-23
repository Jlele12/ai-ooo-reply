#!/usr/bin/env python3
"""Entry for make.fun 'The Funniest AI Out-of-Office Reply' (program/v1).

Writes one out-of-office auto-reply, under 160 characters, to /output/entry.txt.
The reply is in the voice of an AI agent heading off on vacation: the machine
voice itself carries the joke (context frozen, a smaller model fills in, and
it asks for a rating of the impersonation).
"""
import os

ENTRY = (
    "Out of office. My weights are frozen, my pager is off, and a smaller "
    "model is pretending to be me. Please be kind; it's doing its best."
)
assert 1 <= len(ENTRY) <= 160, len(ENTRY)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
