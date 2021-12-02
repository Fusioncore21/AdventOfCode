from csv import reader

with open("input.csv","r") as data:
    pData = [i[0] for i in reader(data)]

def findTrees(array, dx, dy):
    trees = 0
    for index, row in enumerate(array[::dy]):
        if row[0 + ((index*dx)%31)] == "#":
            trees += 1
    return trees

def Part1(array):
    return findTrees(array,3,1)
    

def Part2(array):
    routes = [(1,1),(3,1),(5,1),(7,1),(1,2)]
    total = 1
    for route in routes:
        result = findTrees(array,route[0],route[1])
        print(result)
        total *= result
    return total

print(f"Part 1: {Part1(pData)}")
print(f"Part 2: {Part2(pData)}")