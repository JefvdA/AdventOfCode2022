#! /usr/bin/env python3
"""
Author: Jef van der Avoirt
"""
import os.path
import pytest
from timeit import timeit


INPUT_PATH = os.path.join(os.path.dirname(__file__), "input.txt")


class Folder():
    def __init__(self, name: str, parent: "Folder") -> None:
        self.name = name
        self.folders = []
        self.files = []
        self.parent = parent

    def __str__(self) -> str:
        return f"{self.name} ({len(self.folders)} folders, {len(self.files)} files) total size: {self.get_size()}"

    def add_folder(self, folder: "Folder") -> None:
        self.folders.append(folder)

    def get_size(self) -> int:
        return sum(file.get_size() for file in self.files) + sum(folder.get_size() for folder in self.folders)


class File():
    def __init__(self, name: str, size: int, parent: "Folder") -> None:
        self.name = name
        self.size = size
        self.parent = parent

    def __str__(self) -> str:
        return f"{self.name} ({self.size} bytes)"

    def get_size(self) -> int:
        return self.size


def compute(s: str) -> int:
    lines = s.splitlines()

    all_folders = []
    root = Folder("/", None)
    current_folder = root

    for line in lines:
        if line.startswith("$ cd "):
            folder_name = line[5:]

            if folder_name == "/":
                current_folder = root
            elif folder_name == "..":
                current_folder = current_folder.parent
            else:
                for folder in current_folder.folders:
                    if folder.name == folder_name:
                        current_folder = folder
                        break
                else:
                    raise ValueError(f"Folder {folder_name} not found")
        elif not line.startswith("$ ls"):
            property, name = line.split(" ")
            if property == "dir":
                new_folder = Folder(name, current_folder)
                current_folder.add_folder(new_folder)
            else:
                new_file = File(name, int(property), current_folder)
                current_folder.files.append(new_file)

    all_folders = get_all_folders(root)

    sum = 0
    for folder in all_folders:
        if folder.get_size() < 100000:
            sum += folder.get_size()

    return sum


def get_all_folders(folder: Folder) -> list[Folder]:
    return [folder] + sum((get_all_folders(subfolder) for subfolder in folder.folders), [])


@pytest.mark.parametrize(
    ("sample_input", "expected"),
    (
        # put given test cases here
        ("""\
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k""", 95437),
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
