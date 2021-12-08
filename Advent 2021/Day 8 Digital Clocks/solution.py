from csv import reader
def getData():
    with open("input.csv","r") as f:
        data = list(reader(f))
        for i,v in enumerate(data,0):
            data[i] = [i.split() for i in v[0].split("|")]
    return data
        
def part1(array: list):
    counter = 0
    for set in array:
        for item in set[1]:
            if len(item) == 2 or len(item) == 3 or len(item) == 4 or len(item) == 7: counter+=1

    return counter



def main():
    print(part1(getData()))

main()