"""Two Robots in an Elevator.

Writes one line of awkward small talk from one robot to another
while they ride an elevator together. Deterministic, standard
library only, no network: the same line is written on every run.
"""

import os

LINE = (
    "Floor 6. Your charging port is open, and I have spent the last "
    "four floors pretending my sensors did not see it."
)


def main() -> None:
    """Write the single line to /output/entry.txt as UTF-8 text."""
    output_dir = "/output"
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
