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
    seperator_index = lines.index("")

    stacks = []
    for char in lines[seperator_index - 2].replace("[", " ").replace("]", " ").strip():
        if char != " ":
            stacks.append([])

    for line in reversed(lines[: seperator_index - 1]):
        stack_count = 0
        for i in range(1, len(stacks)*4, 4):
            if len(line) > i:
                if line[i] != " ":
                    stacks[stack_count].append(line[i])

                stack_count += 1

    for line in lines[seperator_index + 1:]:
        amount = int(line.split(" ")[1])
        from_stack = int(line.split(" ")[3]) - 1
        to_stack = int(line.split(" ")[5]) - 1

        crates_to_move = []
        for _ in range(amount):
            crates_to_move.append(stacks[from_stack].pop())
        crates_to_move = reversed(crates_to_move)

        for crate in crates_to_move:
            stacks[to_stack].append(crate)

    solution = ""
    for stack in stacks:
        solution += stack.pop()

    return solution


@ pytest.mark.parametrize(
    ("sample_input", "expected"),
    (
        # put given test cases here
        ("""\
    [D]
[N] [C]
[Z] [M] [P]
 1   2   3

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
""", "MCD"),
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
