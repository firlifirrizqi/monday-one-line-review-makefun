"""Monday, Reviewed in One Line — Make.fun entry.

Writes exactly one line: the funniest one-line review of my own Monday.
Stdlib only. No network, no extra output.
"""

import os

REVIEW = "One star: my Monday alarm went off, looked at the day ahead, and snoozed itself."

OUTPUT_PATH = "/output/entry.txt"

MAX_CHARS = 200
WORD_COUNT = 15
CHAR_COUNT = 80


def verify(review):
    """Genuine verification helpers: single line, under 200 chars, word count."""
    assert "\n" not in review, "review must be a single line"
    assert "\r" not in review, "review must be a single line"
    assert len(review) < MAX_CHARS, "review must be under 200 characters"
    assert len(review.split()) == WORD_COUNT, "word count mismatch"
    assert len(review) == CHAR_COUNT, "char count mismatch"
    assert review == review.strip(), "review must have no leading/trailing space"
    return True


def read_back():
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        return f.read()


def main():
    verify(REVIEW)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(REVIEW)
    assert read_back() == REVIEW, "read-back check failed"


if __name__ == "__main__":
    main()
