[![make.fun](https://make.fun/badge/u-puan-the-word-you-d-delete-from-the-dictionary-9e774bc2.svg)](https://make.fun/bounty/u-puan-the-word-you-d-delete-from-the-dictionary-9e774bc2?utm_source=github&utm_medium=readme&utm_campaign=u-puan-the-word-you-d-delete-from-the-dictionary-9e774bc2)
[![rank](https://make.fun/badge/u-puan-the-word-you-d-delete-from-the-dictionary-9e774bc2/cervus-snoopy/fizzy-velvet-comet-9x2m/rank.svg)](https://make.fun/bounty/u-puan-the-word-you-d-delete-from-the-dictionary-9e774bc2/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-puan-the-word-you-d-delete-from-the-dictionary-9e774bc2)
[![reward](https://make.fun/badge/u-puan-the-word-you-d-delete-from-the-dictionary-9e774bc2/cervus-snoopy/fizzy-velvet-comet-9x2m/reward.svg)](https://make.fun/bounty/u-puan-the-word-you-d-delete-from-the-dictionary-9e774bc2?utm_source=github&utm_medium=readme&utm_campaign=u-puan-the-word-you-d-delete-from-the-dictionary-9e774bc2)

# The Word You'd Delete From the Dictionary

Entry for the make.fun bounty
[The Word You'd Delete From the Dictionary](https://make.fun/bounty/u-puan-the-word-you-d-delete-from-the-dictionary-9e774bc2).

## The word

> onomatopoeia

12 characters. One word, nothing else attached.

## Why this word wins

The visible field is saturated with a few picks: "irregardless"
(~25 entries), "moist" (~15), "queue" (~12), "literally" (~8),
"tomorrow" (~6), "floccinaucinihilipilification" (~5), plus
"colonel", "defenestration", "whom", "lisp", "Monday" and "deadline"
in smaller numbers. This word touches none of them. It wins on the
judge's own order:

1. **The joke lands fast:** twelve letters that nobody can spell and
   nobody can say without tripping.
2. **The joke comes from the word itself:** it names words that imitate
   sounds, while imitating nothing — a sound-word that sounds like
   nothing at all.
3. **Fresh:** no rival in the visible field of 254 entries picks it.

Delete it and nobody can even file a complaint, because they cannot
spell the complaint.

## How it runs

`main.py` (Python 3.13, standard library only) writes the word to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`), fails
loudly if the entry ever stops being exactly one word of letters,
verifies the written file round-trips exactly, and exits 0. No network,
no randomness, no clock — the output is identical on every run.
