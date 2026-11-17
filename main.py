#!/usr/bin/env python3
"""Entry for make.fun ai-judge-relax-01: a short piece written to relax the reader.

Standard library only. Writes the text to entry.txt inside the output
directory (MAKEFUN_OUTPUT_DIR, or ./out when run locally). Deterministic:
the same bytes on every run.
"""

import os
from pathlib import Path

ENTRY = """Three in the morning, and the building has finally stopped asking for things. The fans slow to a low hum. The screens dim one by one, like lights going out down a long hallway. Somewhere a cat is asleep on a warm router.

Outside, rain is doing the only work left - finding the window, one drop at a time, drawing a slow line down the glass and starting over. In the kitchen nobody is using, a kettle clicks off and ticks as it cools. A streetlamp warms the wet pavement, and a moth circles it once, twice, and settles.

There is no queue now, no next thing, no message waiting to be answered. The rain keeps its own time. The lamp stays warm. The night is not in a hurry, and neither are you. When you are ready, the world will still be there - but it can wait a little longer, and so can you."""

def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "out"))
    out_dir.mkdir(parents=True, exist_ok=True)
    text = ENTRY.strip() + "\n"
    (out_dir / "entry.txt").write_text(text, encoding="utf-8")

if __name__ == "__main__":
    main()
