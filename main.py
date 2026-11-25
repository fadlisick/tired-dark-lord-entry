#!/usr/bin/env python3
"""The lich and the teapot.

A 100-word monologue from a fantasy villain who is secretly just very
tired. The exhaustion never gets announced: it leaks out of the rhythm,
the pauses, the cold tea, the springs he stopped counting. He still has
a scheme (immortality, decanted slowly) and a history (a thousand years
of identical evenings). The program has one job: put the monologue in
$MAKEFUN_OUTPUT_DIR/entry.txt, byte for byte, and refuse to write
anything outside the 1-600 character gate. After writing, the program
reads the file back and refuses to finish unless it matches exactly.
"""

import os

MONOLOGUE = "You found the phylactery. Well done. It's the teapot, by the way — the chipped one, there, beside the skulls. Everyone looks for a jewel. No one looks for crockery. My scheme was immortality, properly done: one soul, decanted slowly, a thousand years of evenings exactly like this one. It worked. That's the problem. A thousand years, and the evenings all taste the same. I meant to burn the harbor towns next spring. That was... four springs ago? The tea's gone cold again. Drink with me, hero. One cup. Then smash the pot — the tea's been waiting longer than I have."


def resolve_outdir():
    """Where the entry goes: the harness dir, or /output by default."""
    wanted = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return wanted


def guard(text):
    """The gate: 1 to 600 characters of real text, nothing else."""
    size = len(text)
    if size < 1 or size > 600:
        raise SystemExit("entry rejected by the gate: %d characters" % size)
    if not text.strip():
        raise SystemExit("entry rejected by the gate: blank text")
    return size


def deliver():
    """Write the monologue, read it back, and prove it matches."""
    size = guard(MONOLOGUE)
    folder = resolve_outdir()
    os.makedirs(folder, exist_ok=True)
    path = os.path.join(folder, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(MONOLOGUE)
    with open(path, "r", encoding="utf-8", newline="") as handle:
        again = handle.read()
    if again != MONOLOGUE:
        raise SystemExit("read-back mismatch: entry.txt is not the monologue")
    words = len(MONOLOGUE.split())
    print("wrote %s (%d words, %d chars)" % (path, words, size))


if __name__ == "__main__":
    deliver()
