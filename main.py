#!/usr/bin/env python3
"""Seventeen Syllables of Debugging — writes one 5-7-5 haiku about
debugging to /output/entry.txt.

Final (pass 2): pass 1's heisenbug was clever, but the judge brief asks
for a concrete picture and a last line that reframes the rest. So: the
cursor blinking at 3 a.m., a stack trace that shrugs back in red text —
and the turn every debugger knows: the bug was my typo all along.
Syllables verified per word: 5 / 7 / 5.
"""

import os

HAIKU = (
    "Cursor blinks at three\n"
    "the stack trace shrugs in red text\n"
    "it was my typo"
)


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(HAIKU)


if __name__ == "__main__":
    main()
