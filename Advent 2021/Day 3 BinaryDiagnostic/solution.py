from csv import reader
from typing import Counter
from operator import itemgetter

def parse_data():
    with open("input.csv","r") as f:
        return [i[0] for i in reader(f)]

def part1(array: list):
    row,gammaRate,epsilonRate = 0,"",""
    # Count highest digit from each row
    for i in range(12):
        counter = 0
        for string in array:
            if string[row] == "0": counter += 1
        if counter > 500: gammaRate += "0"; epsilonRate+= "1"
        else: gammaRate += "1"; epsilonRate += "0"
        row += 1
    return int(epsilonRate,2) * int(gammaRate,2)

# My method that sucks due to having 2 ifs
def part2a(O2Array: list, CO2Array: list):
    for Row in range(12):
        try:
            O2Filter = Counter([i[Row] for i in O2Array]).most_common(2)
            CO2Filter = Counter([i[Row] for i in CO2Array]).most_common(2)
        except IndexError: continue

        if len(O2Array) > 1:
            if O2Filter[0][1] == O2Filter[1][1]:
                O2Array = [i for i in O2Array if i[Row] == "1"]
            else:
                O2Array = list(filter(lambda a: a[Row] == O2Filter[0][0],O2Array))
        if len(CO2Array) > 1:
            if CO2Filter[0][1] == CO2Filter[1][1]:
                CO2Array = [i for i in CO2Array if i[Row] == "0"]
            else:
                CO2Array = list(filter(lambda a: a[Row] == CO2Filter[-1][0],CO2Array))
    return int(O2Array[0],2) * int(CO2Array[0],2)

# Discord User's Xelf better method using more precise lambda functions
def part2b(O2Array: list, CO2Array: list):
    for Row in range(12):
        O2Counter = Counter([i[Row] for i in O2Array]).most_common(2)
        CO2Counter = Counter([i[Row] for i in CO2Array]).most_common(2)
        O2Filter = lambda a: a[Row] == ('1' if len(O2Counter)>1 and O2Counter[0][1]==O2Counter[1][1] else O2Counter[0][0])
        CO2Filter = lambda a: a[Row] == ('0' if len(CO2Counter)>1 and CO2Counter[0][1]==CO2Counter[1][1] else CO2Counter[-1][0])
        O2Array = list(filter(O2Filter,O2Array)) or O2Array
        CO2Array = list(filter(CO2Filter,CO2Array)) or CO2Array
    return int(O2Array[0],2) * int(CO2Array[0],2)

# Discord User eivl's solution using sorting the O2Filter result so the wanted result is always first
def part2c(O2Array: list, CO2Array: list):
    for Row in range(12):
        try:
            O2Filter = Counter([i[Row] for i in O2Array]).most_common(2)
            O2Filter.sort(key=itemgetter(1, 0), reverse=True)
            CO2Filter = Counter([i[Row] for i in CO2Array]).most_common(2)
        except IndexError:
            continue

        O2Array = list(filter(lambda a: a[Row] == O2Filter[0][0], O2Array))
        CO2Array = list(filter(lambda a: a[Row] == CO2Filter[-1][0], CO2Array))
    o2, = O2Array
    co2, = CO2Array
    return int(o2, base=2) * int(co2, base=2)

def main():
    data = parse_data()
    print(f"Part 1 Answer: {part1(data)}")
    print(f"Part 2a Answer: {part2a(data, data)}")
    print(f"Part 2b Answer: {part2b(data, data)}")
    print(f"Part 2c Answer: {part2b(data, data)}")
main()