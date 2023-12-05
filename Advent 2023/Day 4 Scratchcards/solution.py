def part1(file):
    file = [row.split(":")[1] for row in file] # Remove Card X: 
    total = 0
    for row in file:
        win,card = row.split("|")
        win_numbers = set(win.split()) & set(card.split())
        if (length:=len(win_numbers)) > 0:
           total += 2**(length-1)
    return total

def part1_1line(file):
    return sum([(2**(total:=len(set(row.split("|")[0].split()) & set(row.split("|")[1].split()))-1)) for row in [row.split(":")[1] for row in file] if total>0])

class Card():
    def __init__(self, details):
        pass

def part2(file):
    pass

with open("./Advent 2023/Day 4 Scratchcards/input.txt","r") as raw:
    File = [row.rstrip("\n") for row in raw.readlines()]

print(part1(File))
