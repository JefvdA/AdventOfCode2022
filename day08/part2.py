#! /usr/bin/env python3
"""
Author: Jef van der Avoirt
"""
import os.path
import pytest


INPUT_PATH = os.path.join(os.path.dirname(__file__), "input.txt")


def compute(s: str) -> int:
    lines = s.splitlines()

    trees_visible_list = []

    for y in range(len(lines)):
        if y == 0 or y == len(lines) - 1:
            continue

        for x in range(len(lines[y])):
            if x == 0 or x == len(lines[y]) - 1:
                continue

            trees_visible_left = 0
            trees_visible_right = 0
            trees_visible_up = 0
            trees_visible_under = 0

            trees_left = [int(t) for t in lines[y][:x]]
            trees_right = [int(t) for t in lines[y][x+1:]]
            trees_up = [int(t[x]) for t in lines[:y]]
            trees_under = [int(t[x]) for t in lines[y+1:]]

            for tree in reversed(trees_left):
                trees_visible_left += 1
                if tree >= int(lines[y][x]):
                    break

            for tree in trees_right:
                trees_visible_right += 1
                if tree >= int(lines[y][x]):
                    break

            for tree in reversed(trees_up):
                trees_visible_up += 1
                if tree >= int(lines[y][x]):
                    break
            
            for tree in trees_under:
                trees_visible_under += 1
                if tree >= int(lines[y][x]):
                    break

            trees_visible = trees_visible_left * trees_visible_right * trees_visible_up * trees_visible_under
            trees_visible_list.append(trees_visible)

    return max(trees_visible_list)


@pytest.mark.parametrize(
    ("sample_input", "expected"),
    (
        # put given test cases here
        ("""\
30373
25512
65332
33549
35390""", 8),
    ),
)
def test_compute(sample_input: str, expected: int) -> None:
    assert compute(sample_input) == expected


def main():
    with open(INPUT_PATH) as f:
        print(compute(f.read()))


if __name__ == "__main__":
    main()
