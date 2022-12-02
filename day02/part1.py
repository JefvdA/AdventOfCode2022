#! /usr/bin/env python3
"""
Author: Jef van der Avoirt
"""
import enum
import os.path
import pytest


INPUT_PATH = os.path.join(os.path.dirname(__file__), "input.txt")


class Options(enum.Enum):
    Rock = 1
    Paper = 2
    Scissors = 3

    def __int__(self):
        return self.value


ENEMY_TURNS = {
    'A': Options.Rock,
    'B': Options.Paper,
    'C': Options.Scissors,
}

MY_TURNS = {
    'X': Options.Rock,
    'Y': Options.Paper,
    'Z': Options.Scissors,
}


def compute(s: str) -> int:
    my_score = 0
    for line in s.splitlines():
        enemy_turn, my_turn = line.split()
        enemy_turn, my_turn = ENEMY_TURNS[enemy_turn], MY_TURNS[my_turn]

        my_score += int(my_turn)

        if my_turn == enemy_turn:
            my_score += 3
        elif my_turn == Options.Rock and enemy_turn == Options.Scissors:
            my_score += 6
        elif my_turn == Options.Paper and enemy_turn == Options.Rock:
            my_score += 6
        elif my_turn == Options.Scissors and enemy_turn == Options.Paper:
            my_score += 6

    return my_score


@pytest.mark.parametrize(
    ("sample_input", "expected"),
    (
        # put given test cases here
        ('''\
A Y
B X
C Z
''', 15),
    ),
)
def test_compute(sample_input: str, expected: int) -> None:
    assert compute(sample_input) == expected


def main():
    with open(INPUT_PATH) as f:
        print(compute(f.read()))


if __name__ == "__main__":
    main()
