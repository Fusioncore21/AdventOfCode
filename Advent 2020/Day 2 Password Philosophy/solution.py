from csv import reader
with open("input.csv","r") as data:
    pData = [i[0] for i in reader(data)]


print(pData)