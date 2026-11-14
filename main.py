"""news-image-01 entry v2: emit one news summary image.

Stdlib only, no network, deterministic: the program copies the exact bytes
of entry.png beside it to $MAKEFUN_OUTPUT_DIR/entry.png on every run.

v2: dense broadsheet infographic — 26 verified stories, 6 continents,
numbered world map, sources footer; lead story FAA ground stop.

Gate constraints (verified): the image is a whole PNG of 200,312 bytes
(at most 1 MiB) and 1024 by 1024 pixels (at most 1024 by 1024).
"""

import os
import shutil


def main():
    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(outdir, exist_ok=True)
    src = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
    # v2: byte-identical copy on every run; no rendering at grade time.
    shutil.copyfile(src, os.path.join(outdir, "entry.png"))


if __name__ == "__main__":
    main()
