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

    for i in range(9):
        head_positions_list = calculate_tail_positions(head_positions_list)
        print(f"Tail #{i}: {len(set(head_positions_list))}")

    return len(set(head_positions_list))


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


def make_board(position_list):
    board = ""
    for y in range(max(position[1] for position in position_list), min(position[1] for position in position_list) - 1, -1):
        for x in range(min(position[0] for position in position_list), max(position[0] for position in position_list) + 1):
            if (x, y) in position_list:
                board += "#"
            else:
                board += "."
        board += "\n"
    return board


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
R 2""", 1),
        ("""\
R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20""", 36)
    ),
)
def test_compute(sample_input: str, expected: int) -> None:
    assert compute(sample_input) == expected


def main():
    with open(INPUT_PATH) as f:
        print(compute(f.read()))


if __name__ == "__main__":
    main()
