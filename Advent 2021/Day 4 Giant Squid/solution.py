from csv import reader
import numpy as np

def parse_data():
    toReturn = []
    with open("testinput.csv","r") as d:
        data = [i for i in reader(d) if i]
        n = data.pop(0)
        data = [i[0].split() for i in data]
        for i in range(0,len(data),5):
            toReturn.append(data[0+i:5+i])
    return toReturn, n

def part1(array: list, numbers: list):
    for number in numbers:
        for index1,bingoCard in enumerate(array,0):
            for index2, row in enumerate(bingoCard,0): 
                row = list(filter(lambda a: a!=number, row))
                # Check if the filter has caused a Bingo
                print(number, array[2][0])
                if not bool(row): return sum([sum(list(map(int,a))) for a in bingoCard]) * int(number)
                # If the row isn't bingo'd, what about the columns?
                array[index1][index2] = row

def part1a(boards, draws):
    board_indices = draws.argsort()[boards]
    win_turn = np.minimum(board_indices.max(axis=1).min(axis=1), board_indices.max(axis=2).min(axis=1))
    win_ind = win_turn.argmin()
    first_win_turn = win_turn[win_ind]
    winning_board = boards[win_ind].reshape(-1, 1)
    winning_board[(winning_board == draws[:first_win_turn+1].reshape(1, -1)).any(axis=1)] = 0
    lose_ind = win_turn.argmax()
    last_win_turn = win_turn[lose_ind]
    losing_board = boards[lose_ind].reshape(-1, 1)
    losing_board[(losing_board == draws[:last_win_turn + 1].reshape(1, -1)).any(axis=1)] = 0
    return winning_board.sum() * draws[first_win_turn], losing_board.sum() * draws[last_win_turn]

def part2():
    ...

def main():
    print(part1(parse_data()[0],parse_data()[1]))
    print(part1a(parse_data()[0],parse_data()[1]))

main()