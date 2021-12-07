from csv import reader

def getData():
    with open("testinput.csv","r") as f:
        return list(map(int,list(reader(f))[0]))

print(getData().sort())