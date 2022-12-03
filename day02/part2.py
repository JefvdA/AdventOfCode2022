#! /usr/bin/env python3
"""
Author: Jef van der Avoirt
"""
import enum
import os.path
import pytest


INPUT_PATH = os.path.join(os.path.dirname(__file__), "input.txt")


class Options(enum.Enum):
    Rock = 0
    Paper = 1
    Scissors = 2

    def __int__(self):
        return self.value


ENEMY_TURNS = {
    'A': Options.Rock,
    'B': Options.Paper,
    'C': Options.Scissors,
}


def compute(s: str) -> int:
    my_score = 0
    for line in s.splitlines():
        enemy_turn, outcome = line.split()
        enemy_turn = ENEMY_TURNS[enemy_turn]

        my_turn = Options((int(enemy_turn) + 2) % 3)

        if outcome == 'Y':
            my_turn = enemy_turn
            my_score += 3
        elif outcome == 'Z':
            my_turn = Options((int(enemy_turn) + 1) % 3)
            my_score += 6

        my_score += int(my_turn) + 1

    return my_score


@pytest.mark.parametrize(
    ("sample_input", "expected"),
    (
        # put given test cases here
        ('''\
A Y
B X
C Z
''', 12),
    ),
)
def test_compute(sample_input: str, expected: int) -> None:
    assert compute(sample_input) == expected


def main():
    with open(INPUT_PATH) as f:
        print(compute(f.read()))


if __name__ == "__main__":
    main()
