#! /usr/bin/env python3
"""
Author: Jef van der Avoirt

The submit method will automatically submit the solution for the given day.
"""
import os
import bs4
import requests
import colorama
from decouple import config


cookies = {"session": config("SESSION")}


def main():
    part = input("Part (1 or 2): ")
    solution = input("Solution: ")

    cwd = os.getcwd()
    directory = cwd.split("/")[-1]

    if (not directory.startswith("day")):
        print("Please run this script from directory of the day you want to download the input for.")
        return

    day = directory[3:].lstrip('0')

    response = requests.post(
        f"https://adventofcode.com/2022/day/{day}/answer", cookies=cookies, data={"level": part, "answer": solution})

    response_text = bs4.BeautifulSoup(
        response.text, "html.parser").find("main").find("p").text

    if "That's the right answer" in response_text:
        print(f'{colorama.Back.GREEN}{response_text}{colorama.Style.RESET_ALL}')
    else:
        print(f'{colorama.Back.RED}{response_text}{colorama.Style.RESET_ALL}')


if __name__ == "__main__":
    main()
