#! /usr/bin/env python3
"""
Author: Jef van der Avoirt
"""
import os.path
import pytest


INPUT_PATH = os.path.join(os.path.dirname(__file__), "input.txt")


def compute(s: str) -> int:

    head_position = (0, 0)

    head_positions_list = [head_position]

    for line in s.splitlines():
        direction, distance = line.split(" ")

        for i in range(int(distance)):
            match direction:
                case "U":
                    head_position = (head_position[0], head_position[1] + 1)
                case "D":
                    head_position = (head_position[0], head_position[1] - 1)
                case "L":
                    head_position = (head_position[0] - 1, head_position[1])
                case "R":
                    head_position = (head_position[0] + 1, head_position[1])

            head_positions_list.append(head_position)

    tail_position_list = calculate_tail_positions(head_positions_list)

    return len(set(tail_position_list))


def calculate_tail_positions(head_position_list):
    tail_position_list = [head_position_list[0]]
    for head_position in head_position_list:
        if head_position[1] > tail_position_list[-1][1] + 1:
            tail_position_list.append((head_position[0], head_position[1] - 1))
        elif head_position[1] < tail_position_list[-1][1] - 1:
            tail_position_list.append((head_position[0], head_position[1] + 1))
        elif head_position[0] > tail_position_list[-1][0] + 1:
            tail_position_list.append((head_position[0] - 1, head_position[1]))
        elif head_position[0] < tail_position_list[-1][0] - 1:
            tail_position_list.append((head_position[0] + 1, head_position[1]))
    
    return tail_position_list



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
