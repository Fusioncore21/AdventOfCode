import csv

with open("input.csv","r") as data:
    pData = [int(i[0]) for i in csv.reader(data)]

# Part 1: Check if next value in list is larger than previous.
def sumChecker(array: list):
    counter = 0
    for i in range(0, len(array)):
        try:
            previous = array[i - 1]
            if array[i] > previous:
                counter += 1
        except IndexError: pass
    return counter

# Part 2: Sum index n with index n+1 amd +2
# Demon summoning level of hellspawn that is this list comprehension
summed_data = [sum([pData[i],pData[i+1],pData[i+2]]) for i in range(0,len(pData)-2)]

print(sumChecker(pData))
print(sumChecker(summed_data))