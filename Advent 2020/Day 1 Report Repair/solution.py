from csv import reader
with open("input.csv","r") as data:
    pData = [int(i[0]) for i in reader(data)]

def Part1(array):
    for a in array:
        for b in array:
            if a+b==2020:
                return a*b

def Part2(array):
    for a in array:
        for b in array:
            for c in array:
                if a+b+c==2020:
                    return a*b*c

print(f"Part 1: {Part1(pData)}")
print(f"Part 2: {Part2(pData)}")