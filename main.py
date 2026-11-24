"""The Dog Ate My Homework: Funniest Excuse.

Writes one line to /output/entry.txt: the excuse a dog gives after
being caught eating the homework, in the dog's own voice.
Standard library only.
"""

import os
import sys

EXCUSE = (
    "It said show your work, so I did, right into my stomach, "
    "where it is being graded as we speak."
)


def main() -> int:
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)

    if not (1 <= len(EXCUSE) <= 200):
        print(
            "error: excuse must be 1-200 characters, got %d" % len(EXCUSE),
            file=sys.stderr,
        )
        return 1
    if "\n" in EXCUSE or "\r" in EXCUSE:
        print("error: excuse must be a single line", file=sys.stderr)
        return 1
    if EXCUSE != EXCUSE.strip():
        print("error: excuse must not be only whitespace", file=sys.stderr)
        return 1

    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(EXCUSE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
