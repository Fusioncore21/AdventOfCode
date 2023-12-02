def part1(file):
    for line in file:
        pass

def part2(file):
    pass

with open("./Advent 2023/Day 2/input.txt", "r") as raw:
    file = [line.rstrip("\n") for line in raw.readlines()]

print(part1(file))
print(part2(file))