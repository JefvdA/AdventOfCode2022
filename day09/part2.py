#! /usr/bin/env python3
"""
Author: Jef van der Avoirt

For some reason, this puzzle fails for the test case... but works for the real puzzle input.
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


knots = [[0, 0] for _ in range(10)]


def compute(s: str) -> int:
    global knots

    tail_positions = set()
    tail_positions.add(tuple(knots[-1]))

    for line in s.splitlines():
        direction, distance = line.split(" ")

        x, y = DIR_DICTIONARY[direction]
        for _ in range(int(distance)):
            move(x, y)
            tail_positions.add(tuple(knots[-1]))

    return len(tail_positions)


def are_touching(x1, y1, x2, y2):
    return abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1


def move(x, y):
    global knots

    knots[0][0] += x
    knots[0][1] += y

    for i in range(1, 10):
        hx, hy = knots[i - 1]
        tx, ty = knots[i]

        if (not are_touching(hx, hy, tx, ty)):
            tx += 0 if hx == tx else (hx - tx) / abs(hx - tx)
            ty += 0 if hy == ty else (hy - ty) / abs(hy - ty)
        
        knots[i] = [tx, ty]


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
R 2""", 1),
        ("""\
R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20""", 36)
    ),
)
def test_compute(sample_input: str, expected: int) -> None:
    assert compute(sample_input) == expected


def main():
    with open(INPUT_PATH) as f:
        print(compute(f.read()))


if __name__ == "__main__":
    main()
