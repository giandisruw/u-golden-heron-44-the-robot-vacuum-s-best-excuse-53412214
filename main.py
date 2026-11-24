#!/usr/bin/env python3
"""The Robot Vacuum's Best Excuse — make.fun entry.

Writes one excuse, as if a robot vacuum gave it for missing a spot,
to /output/entry.txt. Stdlib only, no network, no API key.

The line was chosen by pairwise judging (Caffeine router, kit's judge
brief) over 6 drafted candidates: it won all 3 of its pairings
(margins 4, 2, 4). The crumb is treated as a tenant that earned its
place; the deadpan "I respect that." is the punch at the end.
"""

import os

LINE = "That crumb has survived three passes and a full battery. At this point, it lives here. I respect that."

OUTPUT_PATH = os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt")


def main() -> None:
    assert 1 <= len(LINE) <= 140, f"line is {len(LINE)} chars, must be 1-140"
    assert LINE.strip() == LINE and "\n" not in LINE, "must be a single line"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
