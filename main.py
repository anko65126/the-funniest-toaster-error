"""Entry program for the 'The Funniest Toaster Error Message' make.fun
bounty.

The entry is one line, 1 to 120 characters: the error message a
kitchen toaster shows its owner when something goes wrong. This one
reports that the bread was not found, that it toasted the void
instead, and suggests the owner unplug it and reflect on their
choices. The program writes exactly that one line to /output/entry.txt
(an optional first argument overrides the destination for a dry run).
"""

import sys
from pathlib import Path

LINE = (
    "ERROR 404: Bread not found. I toasted the void instead. Please "
    "unplug me and reflect on your choices."
)
DEFAULT_TARGET = Path("/output/entry.txt")


def main(argv):
    assert 1 <= len(LINE) <= 120, "entry must be 1-120 characters"
    assert LINE.strip() and "\n" not in LINE, "entry must be one line"
    target = Path(argv[1]) if len(argv) > 1 else DEFAULT_TARGET
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(LINE + "\n", encoding="utf-8")
    # Deterministic: the same bytes on every run, no randomness or I/O
    # beyond the single output file.
    assert target.read_text(encoding="utf-8") == LINE + "\n", "round-trip check failed"
    print(f"wrote {target} ({len(LINE)} chars)")


if __name__ == "__main__":
    main(sys.argv)
