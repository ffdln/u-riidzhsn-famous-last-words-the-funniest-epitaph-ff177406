#!/usr/bin/env python3
"""Famous Last Words: The Funniest Epitaph — one line.

The entry is a single fixed epitaph, written for make.fun
u-riidzhsn-famous-last-words-the-funniest-epitaph-ff177406: one line
of famous last words, a tombstone epitaph of at most 150 characters.
A man who dismissed his illness, a doctor who agreed with him, and
a punchline neither of them saw coming. This program writes that
line to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt
outside the grader's container):

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

Python 3.13, standard library only. The epitaph is fixed text:
the same bytes on every run, no network.
"""

import os
import sys
from pathlib import Path

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

LINE = (
    "I told the doctor it was just a cold. He agreed. "
    "We were both wrong \u2014 and now I'm the punchline."
)


def abort(message):
    """Stop with the reason on stderr and a non-zero exit."""
    print(f"main.py: {message}", file=sys.stderr)
    return 1


def deliver():
    """Validate the epitaph against the gate, then write it out."""
    if not 1 <= len(LINE) <= 150:
        return abort(f"epitaph is {len(LINE)} characters, the gate allows 1-150")
    if not LINE.strip():
        return abort("epitaph is only white space, the gate refuses it")
    if "\n" in LINE or "\r" in LINE:
        return abort("epitaph must be a single line, the gate refuses line breaks")
    target = Path(OUTPUT_DIR) / "entry.txt"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(LINE, encoding="utf-8")
    print(f"wrote {target}: {len(LINE)} characters")
    return 0


if __name__ == "__main__":
    raise SystemExit(deliver())
