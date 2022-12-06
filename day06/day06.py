# https://adventofcode.com/2022/day/6

with open('input.txt', 'r') as file:
    raw_input = file.read()


# --- Part 1 --- #
def only_unique(string):
    return len(string) == len(set(c for c in string))


def chars_before_start_of_message(string, size):
    for i in range(len(string) - size + 1):
        buffer = raw_input[i: i + size]
        if only_unique(buffer):
            return i + size


print(chars_before_start_of_message(raw_input, 4))

# --- Part 2 --- #
print(chars_before_start_of_message(raw_input, 14))
