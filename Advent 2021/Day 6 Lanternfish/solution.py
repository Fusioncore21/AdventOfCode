from csv import reader
from typing import Counter

class Lanternfish:
    array = []

    def __init__(self, timer):
        self.timer = int(timer)

    def Tick(self):
        if self.timer == 0:
            Lanternfish.array.append(Lanternfish(9))
            self.timer = 7
        self.timer -= 1

def getData():
    with open("input.csv","r") as f:
        data = list(map(int,list(reader(f))[0]))
        Lanternfish.array = list(map(Lanternfish,data)) # Pt. 1 data
        # Pt. 2 data
        counter = Counter(data)
        dicti = {i:0 for i in range(9)}
        dicti.update(counter)
        return dicti

def part1(): # Solution using a class
    for day in range(80):
        #print([fish.timer for fish in Lanternfish.array])
        for fish in Lanternfish.array:
            #breakpoint()
            fish.Tick()
    return len(Lanternfish.array)

def part2(counter: dict): # As the algorithm basically dies due to having such a long list, lets use a dict
    for day in range(256):
        temp_day = counter.copy()
        print([temp_day[i] for i in range(9)])
        for i in range(8,-1,-1):
            if i:
                counter[i-1] += temp_day[i]
            else:
                counter[6] += temp_day[i]
                counter[8] += temp_day[i]
            counter[i] -= temp_day[i]
    return sum([counter[i] for i in counter.keys()])
            

def main():
    a = getData()
    print(a)
    #print(f"Part 1: {part1()}")
    print(f"Part 2: {part2(a)}")

main()