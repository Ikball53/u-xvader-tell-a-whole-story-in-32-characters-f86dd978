#!/usr/bin/env python3
"""One-line story, told as a Wi-Fi network name.

The brief asks for a whole story in 32 characters. The network name
below is the entire story: an ex who walked out, took the Wi-Fi with
them, and took the dog too. Nothing else is needed — every word in the
name carries a piece of the breakup, and the SSID is the punchline.
"""

import os
from pathlib import Path

# The whole story, as a Wi-Fi network name (SSID).
LINE = "MyExTookTheWiFiAndTheDog"

# The competition caps the line at 32 characters; it must not be empty.
assert 1 <= len(LINE) <= 32, f"line must be 1-32 chars, got {len(LINE)}"


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(LINE + "\n", encoding="utf-8")
    print(f"wrote {len(LINE)}-char story to {target}")


if __name__ == "__main__":
    main()
