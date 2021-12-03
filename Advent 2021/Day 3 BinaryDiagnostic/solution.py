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
        if counter > 500: gammaRate += "0"
        else: gammaRate += "1"
        row += 1
    # Flip values of gammaRate to get epsilonRate
    for i in gammaRate:
        if i == "0": epsilonRate += "1"
        else: epsilonRate += "0"
    
    return int(epsilonRate,2) * int(gammaRate,2)
    



def part2(array):
    ...

def main(): 
    print(f"Part 1 Answer: {part1(parse_data())}")
    print(f"Part 2 Answer: {part2(parse_data())}")

main()