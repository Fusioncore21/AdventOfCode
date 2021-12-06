from csv import reader

class Lanternfish:
    array = []

    def __init__(self, timer):
        self.timer = int(timer)

    def __str__(self):
        return(f"Current Tick: {self.timer}")

    def Tick(self):
        if self.timer == 0:
            Lanternfish.array.append(Lanternfish(9))
            self.timer = 7
        self.timer -= 1

def getData():
    with open("input.csv","r") as f:
        Lanternfish.array = list(map(Lanternfish,list(reader(f))[0]))
        return True

def part1():
    for _ in range(256):
        #print([fish.timer for fish in Lanternfish.array])
        for fish in Lanternfish.array:
            #breakpoint()
            fish.Tick()
    return len(Lanternfish.array)

def main():
    getData()
    print(f"Part 1: {part1()}")

main()