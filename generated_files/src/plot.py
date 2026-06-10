#!/usr/bin/env python3

from pathlib import Path
import sys

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit(f"usage: {Path(sys.argv[0]).name} OUTPUT.png")

    output = Path(sys.argv[1])
    output.parent.mkdir(parents=True, exist_ok=True)

    xs = list(range(0, 7))
    ys = [x * x for x in xs]

    fig, ax = plt.subplots(figsize=(4.8, 3.0), layout="constrained")
    ax.plot(xs, ys, marker="o")
    ax.set_title("Generated quadratic data")
    ax.set_xlabel("x")
    ax.set_ylabel("x squared")
    ax.grid(True, alpha=0.3)
    fig.savefig(output, dpi=160)


if __name__ == "__main__":
    main()
