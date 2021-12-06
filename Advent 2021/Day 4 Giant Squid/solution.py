from csv import reader

def save_data(array: list):
    Counter = 0
    with open("output.txt","w") as f:
        for bingoCard in array:
            for row in bingoCard:
                f.write(f"{row}\n")
                Counter+=1
                if Counter%5==0: f.write("\n"); Counter = 0


    return True

def parse_data():
    toReturn = []
    with open("input.csv","r") as d:
        data = [i for i in reader(d) if i]
        n = data.pop(0)
        data = [i[0].split() for i in data]
        for i in range(0,len(data),5):
            toReturn.append(data[0+i:5+i])
    return toReturn, n

def part1(array: list, numbers: list):
    for number in numbers:
        for index1,bingoCard in enumerate(array,0):
            for index2, row in enumerate(bingoCard,0): 
                row = list(filter(lambda a: a!=number, row))
                # Check if the filter has caused a Bingo
                if not bool(row): return sum([sum(list(map(int,a))) for a in bingoCard]) * int(number)
                # If the row isn't bingo'd, what about the columns?
                array[index1][index2] = row
            #save_data(array)
            #input()

def part2():
    ...

def main():
    print(part1(parse_data()[0],parse_data()[1]))

main()