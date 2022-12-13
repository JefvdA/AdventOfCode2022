#! /usr/bin/env python3
"""
Author: Jef van der Avoirt
"""
import os.path
import pytest


INPUT_PATH = os.path.join(os.path.dirname(__file__), "input.txt")


def compute(s: str) -> int:
    return 0


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
