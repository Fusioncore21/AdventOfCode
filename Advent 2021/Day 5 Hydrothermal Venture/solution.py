from csv import reader

def getData():
    with open("testinput.csv", "r") as f:
        data = list(reader(f))
        data = [i[0].split(" -> ") for i in data]
        return data

def main():
    print(getData())

main()