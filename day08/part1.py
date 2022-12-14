#! /usr/bin/env python3
"""
Author: Jef van der Avoirt
"""
import os.path
import pytest
from timeit import timeit


INPUT_PATH = os.path.join(os.path.dirname(__file__), "input.txt")


def compute(s: str) -> int:
    lines = s.splitlines()

    visible_count = 0

    for y in range(len(lines)):
        if y == 0 or y == len(lines) - 1:
            visible_count += len(lines[y])
            continue

        for x in range(len(lines[y])):
            if x == 0 or x == len(lines[y]) - 1:
                visible_count += 1
                continue

            visible_left = all(int(lines[y][x]) > int(t) for t in lines[y][:x])
            visible_right = all(int(lines[y][x]) > int(t)
                                for t in lines[y][x+1:])
            visible_up = all(int(lines[y][x]) > int(t[x]) for t in lines[:y])
            visible_under = all(int(lines[y][x]) > int(t[x])
                                for t in lines[y+1:])

            if visible_left or visible_right or visible_up or visible_under:
                visible_count += 1

    return visible_count


@pytest.mark.parametrize(
    ("sample_input", "expected"),
    (
        # put given test cases here
        ("""\
30373
25512
65332
33549
35390""", 21),
    ),
)
def test_compute(sample_input: str, expected: int) -> None:
    assert compute(sample_input) == expected


def main():
    with open(INPUT_PATH) as f:
        ex_time = timeit(lambda: print(compute(f.read())), number=1)
    print(f"Execution time: {ex_time:.3f} seconds")


if __name__ == "__main__":
    main()
