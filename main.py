"""One-liner entry: a Wi-Fi network name that tells a whole story in 32 chars.

The name is the whole entry. It is written to entry.txt inside the
output directory so the grader can read it as plain text.
"""

import os
from pathlib import Path

LINE = "MyExTookTheWiFiAndTheDog"

# The competition caps the name at 32 characters; ours is 24, so there is
# room to spare — the joke lands without needing the full budget.
assert 1 <= len(LINE) <= 32, f"LINE must be 1-32 chars, got {len(LINE)}"

OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

OUTPUT_DIR.joinpath("entry.txt").write_text(LINE + "\n", encoding="utf-8")

print(f"Wrote entry: {LINE!r} ({len(LINE)} characters)")
