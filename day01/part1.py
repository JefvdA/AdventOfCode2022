#! /usr/bin/env python3
"""
Author: Jef van der Avoirt
"""
import os.path
import pytest


INPUT_PATH = os.path.join(os.path.dirname(__file__), "input.txt")


def compute(s: str) -> int:
    calories = []
    total_calories = []
    for line in iter(s.splitlines()):
        if line == "":
            sum = calculate_total(calories)
            total_calories.append(sum)
            calories = []
            continue

        calories.append(int(line))

    sum = calculate_total(calories)
    total_calories.append(sum)

    return max(total_calories)


def calculate_total(calories) -> int:
    sum = 0
    for calorie in calories:
        sum += calorie
    return sum


@pytest.mark.parametrize(
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
