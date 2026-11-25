#!/usr/bin/env python3
"""The Dog Ate My Homework: Funniest Excuse — write the entry to /output/entry.txt.

The entry is a single funny line (gate: UTF-8, 1-200 characters, one line,
not only whitespace). It lives in exactly one place, ENTRY_TEXT, so the
text the program writes is the text that was picked — never rebuilt or
reformatted at write time.
"""
import os

# The entry, verbatim. 96 characters, one line. Do not edit the wording
# here without re-running the gate check below and the three self-test
# rounds: the judge compares this exact text, byte for byte.
ENTRY_TEXT = "You said hand it in. I did. In person. Inside me. You never said which person had to hand it in."


def main():
    # Gate self-check: fail loudly rather than submit a different line.
    if not 1 <= len(ENTRY_TEXT) <= 200:
        raise ValueError("entry must be 1-200 characters")
    if "\n" in ENTRY_TEXT or ENTRY_TEXT.strip() == "":
        raise ValueError("entry must be a single non-blank line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT)

if __name__ == "__main__":
    main()
