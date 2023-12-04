import re


def part1(file):
    file = [row.split(": ")[1] for row in file] # Remove Game X: 
    total = 0
    for row in file:
        win,card = row.split(" | ")
        win = win.replace("  ", " ").replace(" ", " | ") #Remove double spacing, then replaces spaces with |

        result = list(re.finditer(win,card))
        length = len(result)
        print(f"{win} string | {card} -> {[i.group() for i in result]}")

        if length > 0:
            total += 2**(length-1)

    return total


def part2(file):
    pass

with open("./Advent 2023/Day 4 Scratchcards/input.txt","r") as raw:
    File = [row.rstrip("\n") for row in raw.readlines()]

print(part1(File))