#!/usr/bin/env python3
"""Inline the stylesheets into index.html to produce a single self-contained
file — one thing to open, email, or drop on a host, with zero external
requests (the IBM Plex faces are already embedded as data URIs).

    python3 build.py            -> dist/index.html

Pass --fragment to also emit dist/fragment.html: the same page with the
doctype/head/body scaffolding stripped, for hosts that supply their own.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).parent
DIST = ROOT / "dist"


def inline(html: str) -> str:
    """Replace each <link rel=stylesheet href=...> with an inline <style>."""

    def sub(m: re.Match) -> str:
        href = m.group(1)
        css = (ROOT / href).read_text(encoding="utf-8")
        return f"<style>\n{css}\n</style>"

    out, n = re.subn(
        r'<link[^>]*rel="stylesheet"[^>]*href="([^"]+)"[^>]*/?>', sub, html
    )
    if n == 0:
        sys.exit("error: no stylesheet links found in index.html")
    print(f"  inlined {n} stylesheet(s)")
    return out


def main() -> None:
    html = (ROOT / "index.html").read_text(encoding="utf-8")
    DIST.mkdir(exist_ok=True)

    full = inline(html)
    (DIST / "index.html").write_text(full, encoding="utf-8")
    print(f"  dist/index.html  {len(full.encode()):,} bytes")

    if "--fragment" in sys.argv:
        # Keep <title> and <style>, drop the document scaffolding.
        title = re.search(r"<title>.*?</title>", full, re.S).group(0)
        styles = "\n".join(re.findall(r"<style>.*?</style>", full, re.S))
        body = re.search(r"<body[^>]*>(.*)</body>", full, re.S).group(1)
        frag = f"{title}\n{styles}\n{body.strip()}\n"
        (DIST / "fragment.html").write_text(frag, encoding="utf-8")
        print(f"  dist/fragment.html  {len(frag.encode()):,} bytes")


if __name__ == "__main__":
    main()
