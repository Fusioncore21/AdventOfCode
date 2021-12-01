import csv

with open("input.csv","r") as data:
    parsed_data = [int(i[0]) for i in csv.reader(data)]


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
summed_data = [sum([parsed_data[i],parsed_data[i+1],parsed_data[i+2]]) for i in range(0,len(parsed_data)-2)]

print(sumChecker(parsed_data))
print(sumChecker(summed_data))