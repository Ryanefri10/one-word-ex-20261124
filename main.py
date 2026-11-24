"""One Word From Your Ex -- make.fun entry.

Writes a single word to /output/entry.txt: the word the entrant's ex
would use to describe them.

The word is "Project". It is the classic ex line -- she took him on
as a project, convinced she could fix him, and he stayed exactly as
he was. It is funny at once, it stings because it is painfully true,
and it needs no explanation: everyone has either been the project or
dated one. Seven characters, inside the 1-24 gate, plain UTF-8, one
word and nothing else.
"""

import os

WORD = "Project"

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    # Enforce the competition's gate here too, so a future word change
    # can never silently produce an invalid entry: 1-24 UTF-8 chars,
    # exactly one word, not only white space.
    text = WORD.strip()
    if not 1 <= len(text) <= 24 or len(text.split()) != 1:
        raise ValueError("entry word violates the 1-24 character gate: %r" % WORD)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
