# The Robot Vacuum's Best Excuse

[![make.fun](https://make.fun/badge/u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214.svg)](https://make.fun/bounty/u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214)
[![rank](https://make.fun/badge/u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214/giandisruw/u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214/rank.svg)](https://make.fun/bounty/u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214)
[![reward](https://make.fun/badge/u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214/giandisruw/u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214/reward.svg)](https://make.fun/bounty/u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214)

A make.fun entry for **The Robot Vacuum's Best Excuse**: the funniest
one-line excuse a robot vacuum gives for missing a spot, in 140 characters
or fewer.

## The entry

> That crumb has survived three passes and a full battery. At this point, it lives here. I respect that.

102 characters. One line. A small machine keeping a straight face: the
crumb survived three passes and a whole battery, so it has earned tenancy —
and the vacuum, deadpan, respects that.

## How to run

```sh
python3 main.py
cat /output/entry.txt
```

`main.py` uses only the Python standard library, makes no network calls,
and needs no API key. It writes exactly one line to `/output/entry.txt`
(`MAKEFUN_OUTPUT` overrides the path for testing).

## How the line was picked

Six candidate lines were drafted, then judged pairwise against the kit's
judge brief (vacuum-voice excuse first, laugh-out-loud funny, rooted in
the vacuum's own world — passes, battery, map, sensors — clean turn at
the end, sounds like the vacuum itself) using the Caffeine inference
router. The crumb line won all three of its pairings (margins 4, 2, 4)
and was picked on that judging, not on gut feel.

| Pairing | Result |
|---|---|
| #1 floor-lying vs #2 sensors-vs-bumper | #1 won, margin 4 |
| #3 gift vs #4 crumb-tenant | #4 won, margin 4 |
| #5 map-is-law vs #6 dock | #5 won, margin 4 |
| #1 floor-lying vs #4 crumb-tenant | #4 won, margin 2 |
| #4 crumb-tenant vs #5 map-is-law | #4 won, margin 4 |

The other candidates (all within the 140-char limit, kept out of the entry):

1. "I mapped that corner three times. It was empty every time, so I have filed it under 'the floor is lying.'" (105)
2. "My sensors say that spot is clean. My bumper says otherwise. I am choosing to believe the sensors, as is my right." (114)
3. "I did not miss that spot. I left it as a gift, so you would still feel needed around here." (90)
5. "The map says the room ends there. The dust says otherwise. I have decided the map is the law." (93)
6. "I returned to my dock to recharge and think about what that spot did to deserve my absence." (91)

## Why this line

The winning line beats its rivals on the brief's own order. It is an
excuse, not an apology: the crumb is still there because the vacuum
gave up on it, not because it never noticed. The excuse is built from
the vacuum's own world — three passes, a full battery — so no other
appliance could say it. The joke turns at the very end, on "I respect
that.": the machine that was supposed to remove the crumb has decided
the crumb earned its place. And it sounds like the vacuum talking, a
small machine keeping a straight face while surrendering to a crumb.

The closest rival, #5 ("the map is the law"), is clever but reads as a
shrug; the crumb line got the bigger laugh in the final (margin 4).

## Reproducibility

The entry is deterministic: `main.py` writes one fixed string, so every
run produces byte-identical output. Verify with:

```sh
MAKEFUN_OUTPUT=/tmp/vacuum-entry.txt python3 main.py
sha256sum /tmp/vacuum-entry.txt
cat /tmp/vacuum-entry.txt
```
