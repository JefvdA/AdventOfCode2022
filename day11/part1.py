#! /usr/bin/env python3
"""
Author: Jef van der Avoirt
"""
import os.path
import pytest
from timeit import timeit


INPUT_PATH = os.path.join(os.path.dirname(__file__), "input.txt")


def parse_input(s: str):
    M = []
    O = []
    TC = []
    CM = []
    WM = []

    for monkey in s.split("\n\n"):
        M.append([int(i) for i in monkey.splitlines()[1][18:].split(", ")])
        O.append(monkey.splitlines()[2][23:])
        TC.append(int(monkey.splitlines()[3][21:]))
        CM.append(int(monkey.splitlines()[4][29:]))
        WM.append(int(monkey.splitlines()[5][30:]))
    
    return M, O, TC, CM, WM


def compute(s: str) -> int:
    M, O, TC, CM, WM = parse_input(s)

    THC = [0]*len(M)

    for i in range(20):
        for i, m in enumerate(M):
            for j in range(len(M[i])):
                # Inspect item : item = item (OPERATION)
                if (O[i].split(" ")[1] == "old"):
                    M[i][j] = eval(f"{M[i][j]} {O[i].split(' ')[0]} {M[i][j]}")
                else:
                    M[i][j] = eval(f"{M[i][j]} {O[i]}")
                # Get bored by item: item = item / 3
                M[i][j] //= 3
                # Test the current Worry lever against the test case (TC)
                if M[i][j] % TC[i] == 0:
                    M[CM[i]].append(M[i][j])
                else:
                    M[WM[i]].append(M[i][j])
                # Add the count for throwing for the current monkey (THC)
                THC[i] += 1
            M[i] = []

    return sorted(THC, reverse=True)[0] * sorted(THC, reverse=True)[1]


@pytest.mark.parametrize(
    ("sample_input", "expected"),
    (
        # put given test cases here
        ("""\
Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1""", 10605),
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
