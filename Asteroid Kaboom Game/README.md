# Asteroid Kaboom

A Python Turtle game that combines randomized graphics with coordinate-based interaction.

[Back to portfolio](../README.md)

## Features

- Random star field and polygon asteroids with varied positions, sizes, and rotations.
- Dialog-based input for shot coordinates.
- Color-based scoring: pink targets award 100 points and purple targets award 10.
- Visual shot effects and a final score display.

## Run

Requires Python 3 with Turtle/Tk support and a graphical desktop. There are no third-party Python package dependencies.

From the repository root:

```bash
cd "Asteroid Kaboom Game"
python "GAME _CODE.py"
```

Keep `pixels.py` beside the main script. If your system uses `python3`, substitute it for `python`.

Enter a shot count, then X and Y coordinates when prompted. Click the game window after the final score to close it.

## Files

| File | Purpose |
| --- | --- |
| `GAME _CODE.py` | Main game, rendering, input, and scoring |
| `pixels.py` | Pixel-color helper used for scoring |
| `kaboom_starter_code.py` | Assignment starter code |

## Implementation notes

The current version expects valid numeric input; cancelling an input dialog is not handled. It is intended to run locally, rather than in a headless terminal.

The helper in `pixels.py` retains its original attribution to Sam Scott and Ethan McMehen and its upstream reference.
