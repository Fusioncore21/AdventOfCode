import re

match_num = re.compile("[0-9]\d+")
match_sym = re.compile("[^\.|0-9]")

def part1(file):
    symbols = [(a,b.start()) for a,b in enumerate(re.finditer(match_sym,row)) for row in file]

    for line in file:
        pass

def part2(file):
    pass

with open("./Advent 2023/Day 3 Gear Ratios/input.txt", "r") as raw:
    File = [line.rstrip("\n") for line in raw.readlines()]

print(part1(File))
print(part2(File))

