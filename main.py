"""Write one bizarre-but-real startup pitch to /output/entry.txt."""

from pathlib import Path

PITCH = (
    "We buy abandoned half-finished knitting, model kits and puzzles for pennies, "
    "then resell them as finish-it kits to crafters paying $29 a month for the "
    "joy of finishing without starting."
)


def main() -> None:
    output = Path("/output/entry.txt")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(PITCH, encoding="utf-8")


if __name__ == "__main__":
    main()
