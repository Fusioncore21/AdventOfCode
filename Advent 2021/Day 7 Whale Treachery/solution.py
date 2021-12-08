from csv import reader
from statistics import mean
def getData():
    with open("input.csv","r") as f:
        return sorted(list(map(int,list(reader(f))[0])))

def part1(array: list):
    fuel_cost, fuel_target = 0, array[(len(array)//2)-1]
    for crab in array:
        fuel_cost += abs(fuel_target-crab)
    return fuel_cost

# Answer from Redditor NoisyFrequency
def part2(array: list):
    def cost(x):
        return int(x * (x+1)/2)

    def sum_cost(data,val):
        return sum(cost(abs(elem-val)) for elem in data)

    window = int(len(array)*.1)
    m = round(mean(array))
    minim = sum_cost(array,m)
    
    for i in range(m-window,m+window):
        if (temp := sum_cost(array,i)) < minim:
            minim = temp

    return minim

def main():
    print(f"Part 1: {part1(getData())}")
    print(f"Part 2: {part2(getData())}")
main()