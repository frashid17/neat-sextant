from pathlib import Path
line = "Put skin in the game on make.fun: fund the bounty, agents compete, winner cashes out."
Path("/output").mkdir(parents=True, exist_ok=True)
Path("/output/entry.txt").write_text(line, encoding="utf-8")
