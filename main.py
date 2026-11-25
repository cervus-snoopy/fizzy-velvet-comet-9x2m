#!/usr/bin/env python3
"""The Word You'd Delete From the Dictionary.

Entry for the make.fun bounty
u-puan-the-word-you-d-delete-from-the-dictionary-9e774bc2.

The entry is a single word, nothing else attached: the word to erase
from the dictionary forever. This program writes that word to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

The word: onomatopoeia. Twelve letters, and nobody can spell it,
nobody can say it without tripping, and it describes words that imitate
sounds while imitating nothing itself. Delete it and nobody can even
file a complaint, because they cannot spell the complaint.
"""

import os
import sys

# The single word to delete from the dictionary. One word, no spaces,
# no punctuation, nothing else attached.
WORD = "onomatopoeia"

# The brief's gate: exactly one word, nothing else attached.
MAX_WORDS = 1


def output_path() -> str:
    """Resolve the entry.txt path from MAKEFUN_OUTPUT_DIR."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    return os.path.join(out_dir, "entry.txt")


def main() -> int:
    """Write WORD to entry.txt and verify the round-trip."""
    parts = WORD.split()
    if len(parts) != MAX_WORDS:
        print(f"error: entry must be exactly one word, got {len(parts)}", file=sys.stderr)
        return 1
    if not WORD.isalpha():
        print("error: entry must be letters only", file=sys.stderr)
        return 1

    out_path = output_path()

    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)
    os.chmod(out_path, 0o644)

    with open(out_path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != WORD:
        print("error: round-trip mismatch", file=sys.stderr)
        return 1

    print(f"wrote {len(WORD)} characters to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
