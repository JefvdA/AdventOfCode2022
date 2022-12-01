#! /usr/bin/env python3
"""
Author: Jef van der Avoirt
"""
import os.path
import pytest


INPUT_PATH = os.path.join(os.path.dirname(__file__), "input.txt")


def compute(s: str) -> int:
    elves = []
    for elve in s.split('\n\n'):
        calories = 0
        for line in elve.splitlines():
            calories += int(line)
        elves.append(calories)

    return max(elves)


@ pytest.mark.parametrize(
    ("sample_input", "expected"),
    (
        # put given test cases here
        ('''\
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000''', 24000),
    ),


)
def test_compute(sample_input: str, expected: int) -> None:
    assert compute(sample_input) == expected


def main():
    with open(INPUT_PATH) as f:
        print(compute(f.read()))


if __name__ == "__main__":
    main()
