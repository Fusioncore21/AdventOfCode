from csv import reader

with open("input.csv", "r") as data:
    pData = [i.strip("\n") for i in data]
    

def part1(data):
    HPos, Depth = 0,0
    for cmd in data:
        split_data = cmd.split()
        if split_data[0] == "forward":
            HPos += int(split_data[1])
        elif split_data[0] == "down":
            Depth += int(split_data[1])
        elif split_data[0] == "up":
            Depth -= int(split_data[1])

    return HPos * Depth

def part2(data):
    Aim, HPos, Depth = 0,0,0
    for cmd in data:
        split_data = cmd.split()
        if split_data[0] == "forward":
            HPos += int(split_data[1])
            Depth += int(split_data[1]) * Aim
        elif split_data[0] == "down":
            Aim += int(split_data[1])
        elif split_data[0] == "up":
            Aim -= int(split_data[1])

    return HPos * Depth
    

print(f"Part 1 Answer: {part1(pData)}")
print(f"Part 2 Answer: {part2(pData)}")