from csv import reader

def parse_data():
    with open("testinput.csv","r") as f:
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

def part2(O2Array,CO2Array):
    for Row in range(0,12):
        # O2 Finding Bit to Filter
        if sum([int(i[Row]) for i in O2Array]) >= len(O2Array) // 2: O2FilterBit = "0"
        else: O2FilterBit = "1"
        #CO2 Finding Bit to Filter
        if sum([int(i[Row]) for i in CO2Array]) <= len(CO2Array) // 2: CO2FilterBit = "1"
        else: CO2FilterBit = "0"
        # Filter Arrays
        

def main(): 
    #print(f"Part 1 Answer: {part1(parse_data())}")
    print(f"Part 2 Answer: {part2(parse_data(),parse_data())}")

main()