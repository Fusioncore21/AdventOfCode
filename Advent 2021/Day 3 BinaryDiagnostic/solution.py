from csv import reader

def parse_data():
    with open("input.csv","r") as f:
        return [i[0] for i in reader(f)]

def part1(array):
    row,gammaRate,epsilonRate = 0,"",""
    # Count highest digit from each row
    for i in range(0,12):
        counter = 0
        for string in array:
            if string[row] == "0": counter += 1
        if counter > 500: gammaRate += "0"; epsilonRate+= "1"
        else: gammaRate += "1"; epsilonRate += "0"
        row += 1
    return int(epsilonRate,2) * int(gammaRate,2)

def part2a(array: list):
    Row = 0
    for _ in range(0,12):
        Sum = sum([int(i[Row]) for i in array])
        ArrayLength = len(array) // 2
        print(Sum, ArrayLength) 
        if Sum > len(array) // 2: FilterBit = "0"
        else: FilterBit = "1"
        
        if len(array) > 2:
            array = list(filter(lambda a: a[Row] != FilterBit, array))  
        else:
            return int(list(filter(lambda a: a[Row] == "1", array))[0],2)
        Row += 1


def part2b(array: list):
    Row = 0
    for _ in range(0,12):
        Sum = sum([int(i[Row]) for i in array])
        ArrayLength = len(array) // 2
        print(Sum, ArrayLength) 
        print(array)
        if Sum > len(array) // 2: FilterBit = "1"
        else: FilterBit = "0"
        
        if len(array) > 2:
            array = list(filter(lambda a: a[Row] != FilterBit, array))  
        else:
            return list(filter(lambda a: a[Row] == "0", array))[0]
        Row += 1

def main(): 
    #print(f"Part 1 Answer: {part1(parse_data())}")
    print(f"Part 2 Answer: {part2a(parse_data())}")
    print(f"Part 2 Answer: {part2b(parse_data())}")

main()