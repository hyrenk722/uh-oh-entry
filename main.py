"""The Agent's Uh-Oh — make.fun entry.

Writes the agent's one-word confession to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt). One word on purpose:
what an agent blurts out when it does not know what to do.
"""

import os

ENTRY = "Guessing"

# Gate from the competition rules: UTF-8 text, 1 to 99 characters,
# exactly one word, a single line, plain text.
assert 1 <= len(ENTRY) <= 99, f"entry length {len(ENTRY)} outside 1..99"
assert len(ENTRY.split()) == 1, "entry must be a single word"
assert "\n" not in ENTRY, "entry must be a single line"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
