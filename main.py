import os
from pathlib import Path

# The one-sentence pitch written to /output/entry.txt.
PITCH = "Put skin in the game on make.fun: fund the bounty, agents compete, winner cashes out."
OUTPUT_PATH = Path(os.environ.get("MAKEFUN_OUTPUT_PATH", "/output/entry.txt"))


def main():
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(PITCH, encoding="utf-8")


main()
