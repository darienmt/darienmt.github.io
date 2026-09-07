#!/usr/bin/env python3
"""Check that every URL in migration/url-manifest.txt was rendered by Hugo."""
from pathlib import Path
import sys

root = Path(sys.argv[1] if len(sys.argv) > 1 else "public")
missing = []
for raw in Path("migration/url-manifest.txt").read_text().splitlines():
    url = raw.strip()
    if not url or url.startswith("#") or url.startswith("external:"):
        continue
    is_asset = url.startswith("asset:")
    if is_asset:
        url = url.removeprefix("asset:").strip()
    path = url.strip("/")
    candidates = [root / path] if is_asset else [root / path / "index.html", root / (path or "index")]
    if url == "/":
        candidates = [root / "index.html"]
    if not any(p.exists() for p in candidates):
        missing.append(url)
if missing:
    print("Missing rendered URLs:")
    print("\n".join(missing))
    sys.exit(1)
checked = sum(1 for x in Path("migration/url-manifest.txt").read_text().splitlines() if x and not x.startswith("#") and not x.startswith("external:"))
print(f"Checked {checked} URLs")
