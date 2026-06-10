#!/usr/bin/env python3

from pathlib import Path
import sys


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit(f"usage: {Path(sys.argv[0]).name} OUTPUT.tex")

    output = Path(sys.argv[1])
    output.parent.mkdir(parents=True, exist_ok=True)

    rows = [(x, x * x, x * x * x) for x in range(1, 6)]
    lines = [
        r"\begin{tabular}{r|rr}",
        r"$x$ & $x^2$ & $x^3$ \\",
        r"\hline",
    ]
    lines.extend(f"{x} & {square} & {cube} \\\\" for x, square, cube in rows)
    lines.append(r"\end{tabular}")

    output.write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
