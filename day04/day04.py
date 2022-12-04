# https://adventofcode.com/2022/day/4

with open('input.txt', 'r') as file:
    raw_input = file.read()
    lines = raw_input.splitlines()


# --- Part 1 --- #


def parse_range(string: str):
    splt_string = string.split('-')
    return int(splt_string[0]), int(splt_string[1])


pairs = [(parse_range(line.split(',')[0]), parse_range(line.split(',')[1]))
         for line in lines]


def fully_contains(range1, range2):
    return range2[0] >= range1[0] and range2[1] <= range1[1]


containings = [pair for pair in pairs if (fully_contains(pair[0], pair[1]) or fully_contains(pair[1], pair[0]))]
print(len(containings))


# --- Part 1 --- #

def overlap(range1, range2):
    return range1[0] <= range2[0] <= range1[1]


overlaps = [pair for pair in pairs if (overlap(pair[0], pair[1]) or overlap(pair[1], pair[0]))]
print(len(overlaps))
