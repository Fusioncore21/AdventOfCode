from csv import reader

def getData():
    with open("testinput.csv", "r") as f:
        data = list(reader(f))
        for i in range(len(data)):
            ...
        return data

def main():
    print(getData())

main()