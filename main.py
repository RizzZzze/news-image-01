"""news-image-01 entry: emit one news summary image.

Stdlib only, no network, deterministic: the program copies the exact bytes
of entry.png beside it to $MAKEFUN_OUTPUT_DIR/entry.png on every run.

Gate constraints (verified): the image is a whole PNG of 895,118 bytes
(at most 1 MiB) and 896 by 896 pixels (at most 1024 by 1024).
"""

import os
import shutil


def main():
    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(outdir, exist_ok=True)
    src = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
    shutil.copyfile(src, os.path.join(outdir, "entry.png"))


if __name__ == "__main__":
    main()
