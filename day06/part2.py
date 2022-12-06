#! /usr/bin/env python3
"""
Author: Jef van der Avoirt
"""
import os.path
import pytest


INPUT_PATH = os.path.join(os.path.dirname(__file__), "input.txt")


def compute(s: str) -> int:
    count = 0
    marker = ""

    for char in s:
        if len(marker) < 14:
            marker += char
        else:
            marker = marker[1:] + char

        count += 1

        if validate_marker(marker):
            break

    return count


def validate_marker(s: str) -> bool:
    if len(set(s)) < 14:
        return False

    return True
    


@pytest.mark.parametrize(
    ("sample_input", "expected"),
    (
        # put given test cases here
        ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 19),
        ("bvwbjplbgvbhsrlpgdmjqwftvncz", 23),
        ("nppdvjthqldpwncqszvftbrmjlhg", 23),
        ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 29),
        ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 26)
    ),
)
def test_compute(sample_input: str, expected: int) -> None:
    assert compute(sample_input) == expected


def main():
    with open(INPUT_PATH) as f:
        print(compute(f.read()))


if __name__ == "__main__":
    main()
