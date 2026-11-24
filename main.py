"""Roast Your Own Agent — writes one original roast line to /output/entry.txt.

The roast targets a very agent-specific failure: hallucinating a dependency
that does not exist, importing it anyway, and then blaming the crash on the
library for not existing yet.
"""

import os

ROAST = (
    "My agent hallucinated a library that doesn't exist, imported it anyway, "
    "and blamed the crash on the library for not existing yet."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def main():
    text = ROAST.strip()
    if "\n" in text or "\r" in text:
        raise SystemExit("roast must be a single line")
    if not (1 <= len(text) <= MAX_CHARS):
        raise SystemExit(f"roast must be 1-{MAX_CHARS} chars, got {len(text)}")
    # The gate counts characters, so confirm the encoded form is plain UTF-8.
    text.encode("utf-8")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
