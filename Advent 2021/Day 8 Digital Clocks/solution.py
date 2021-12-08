from csv import reader
def getData():
    with open("testinput.csv","r") as f:
        data = list(reader(f))
        for i,v in enumerate(data,0):
            data[i] = [i for i in v[0].split("|")]
    return data
        
def part1(array: list):
    counter = 0
    for set in array:
        for item in set[1]:
            if len(item) in {2,3,4,7}: counter+=1
    
    return counter

def part2(array: list):
    ...

def main():
    print(getData())
    #print(part1(getData()))

main()