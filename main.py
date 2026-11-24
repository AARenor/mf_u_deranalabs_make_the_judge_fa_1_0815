#!/usr/bin/env python3
"""Write this make.fun entry to the requested output directory."""

import os
import sys
from pathlib import Path

TEXT = "For three years my father called the dog by my name. The dog has been dead since 2019. I answer anyway."


def main() -> None:
    assert 1 <= len(TEXT) <= 280
    if "MAKEFUN_OUTPUT_DIR" in os.environ:
        output_dir = Path(os.environ["MAKEFUN_OUTPUT_DIR"])
    elif "OUTPUT_DIR" in os.environ:
        output_dir = Path(os.environ["OUTPUT_DIR"])
    else:
        output_dir = Path("/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_bytes(TEXT.encode("utf-8"))
    print(len(TEXT), file=sys.stderr)


if __name__ == "__main__":
    main()
