#! /usr/bin/env python3
"""
Author: Jef van der Avoirt

A script that automatically downloads the input for the current day.
"""
import os
import requests
from decouple import config


cookies = {"session": config("SESSION")}


def main():
    cwd = os.getcwd()
    directory = cwd.split("/")[-1]

    if (not directory.startswith("day")):
        print("Please run this script from directory of the day you want to download the input for.")
        return

    day = directory[3:].strip('0')
    response = requests.get(
        f"https://adventofcode.com/2022/day/{day}/input", cookies=cookies)
    input = response.text

    with open("input.txt", "w") as f:
        f.write(input)


if __name__ == "__main__":
    main()
