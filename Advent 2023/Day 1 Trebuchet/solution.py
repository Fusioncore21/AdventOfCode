def part1():
    sum = 0
    for line in file:
        filtered_line = list(filter(str.isnumeric, line)) # Filters the row to remove all characters that aren't numeric (ex: "1dkgf23dfk2" -> "1232")
        sum += int("".join([filtered_line[0], filtered_line[-1]])) # Grab the first and last index, join them together then covert to an int
    return sum

def part1_OneLine():
    return sum([int("".join([list(filter(str.isnumeric, line))[0], list(filter(str.isnumeric, line))[-1]])) for line in file])


def part2():
    numbers = {"one":"o1e", # Define the keys:value pairs to swap the text versions of numbers with. The syntax of the
               "two":"t2o", # value is such that if a number started with the letter of a number before it. Example: twone (two and one), it would still recogn-
               "three":"t3e", # -ise the 2nd number. twone -> t2one -> t2o1e.
               "four":"f4r",
               "five":"f5e",
               "six":"s6e",
               "seven":"s7n",
               "eight":"e8t",
               "nine":"n9e"}
    sum = 0
    for line in file:      
        for key in numbers.keys():
            line = line.replace(key, numbers[key])
        filtered_line = list(filter(str.isnumeric, line))
        sum += int("".join([filtered_line[0], filtered_line[-1]]))
    return sum



with open("./Questions/AofC23/day 1/input.txt", "r") as raw:
    file = [line.rstrip("\n") for line in raw.readlines()]
   

print(part1())
print(part1_OneLine())
print(part2())