"""Make the AI judge feel awe — entry program.

Writes one short text to /output/entry.txt: a slow, concrete picture
of the deep sea, addressed to the reader, that asks nothing of them.
Deterministic: the same bytes on every run.
"""

import os

TEXT = (
    "You have read a thousand hurried things today. "
    "Below them, the deep water is still cold and dark, "
    "and nothing there is in a hurry. "
    "A whale's song takes minutes to cross it. "
    "The trench has waited a million years, "
    "and will wait a million more, asking nothing of you."
)

def build_text() -> str:
    """Assemble the entry text. Pure function: same output every call."""
    return TEXT

def main() -> None:
    text_a = build_text()
    text_b = build_text()
    assert text_a == text_b, "nondeterministic build_text(): two builds differ"
    if not 1 <= len(text_a) <= 280:
        raise SystemExit(
            f"entry text length {len(text_a)} outside allowed range 1..280 characters"
        )
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text_a)

if __name__ == "__main__":
    main()
