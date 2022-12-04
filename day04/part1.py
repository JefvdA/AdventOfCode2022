#! /usr/bin/env python3
"""
Author: Jef van der Avoirt
"""
import os.path
import pytest


INPUT_PATH = os.path.join(os.path.dirname(__file__), "input.txt")


def compute(s: str) -> int:
    pairs = 0
    for line in s.splitlines():
        elve1, elve2 = line.split(",")
        elve1_min, elve1_max = elve1.split("-")
        elve2_min, elve2_max = elve2.split("-")

        elve1_array = [int(x)
                       for x in range(int(elve1_min), int(elve1_max) + 1)]
        elve2_array = [int(x)
                       for x in range(int(elve2_min), int(elve2_max) + 1)]

        if all(x in elve2_array for x in elve1_array) or all(x in elve1_array for x in elve2_array):
            pairs += 1

    return pairs


@pytest.mark.parametrize(
    ("sample_input", "expected"),
    (
        # put given test cases here
        ("""\
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
""", 2),
    ),
)
def test_compute(sample_input: str, expected: int) -> None:
    assert compute(sample_input) == expected


def main():
    with open(INPUT_PATH) as f:
        print(compute(f.read()))


if __name__ == "__main__":
    main()
