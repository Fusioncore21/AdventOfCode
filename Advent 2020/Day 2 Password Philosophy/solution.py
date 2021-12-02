from csv import reader


# Extract Input Data
with open("input.csv","r") as data:
    pData = [i[0] for i in reader(data)]

# Parse data for needs
for index,inp in enumerate(pData):
    inp = inp.split()
    inp[0] = inp[0].split("-")
    inp[1] = inp[1].removesuffix(":")
    pData[index] = inp

def Part1(array):
    validPasswords = 0
    for policy in array:
        print(policy)
        countedLetters = int(policy[2].count(policy[1]))
        min = int(policy[0][0])
        max = int(policy[0][1])
        if countedLetters >= min and countedLetters <= max:
            validPasswords += 1
    return validPasswords

def Part2(array):
    ...

print(f"Part 1: {Part1(pData)}")
print(f"Part 2: {Part2(pData)}")