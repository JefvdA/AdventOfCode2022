#! /usr/bin/env python3
"""
Author: Jef van der Avoirt
"""
import os.path
import pytest


INPUT_PATH = os.path.join(os.path.dirname(__file__), "input.txt")


DIR_DICTIONARY = {
    "U": (0, 1),
    "D": (0, -1),
    "L": (-1, 0),
    "R": (1, 0)
}


hx, hy = 0, 0
tx, ty = 0, 0


def compute(s: str) -> int:
    global tx, ty

    tail_positions = set()
    tail_positions.add((tx, ty))

    for line in s.splitlines():
        direction, distance = line.split(" ")

        x, y = DIR_DICTIONARY[direction]
        for i in range(int(distance)):
            move(x, y)
            tail_positions.add((tx, ty))

    return len(tail_positions)


def are_touching(x1, y1, x2, y2):
    return abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1


def move(x, y):
    global hx, hy, tx, ty

    hx += x
    hy += y

    if (not are_touching(hx, hy, tx, ty)):
        tx += 0 if hx == tx else (hx - tx) // abs(hx - tx)
        ty += 0 if hy == ty else (hy - ty) // abs(hy - ty)


@pytest.mark.parametrize(
    ("sample_input", "expected"),
    (
        # put given test cases here
        ("""\
R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2""", 13),
    ),
)
def test_compute(sample_input: str, expected: int) -> None:
    assert compute(sample_input) == expected


def main():
    with open(INPUT_PATH) as f:
        print(compute(f.read()))


if __name__ == "__main__":
    main()
