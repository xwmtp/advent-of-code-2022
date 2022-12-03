# https://adventofcode.com/2022/day/3

with open('input.txt', 'r') as file:
    raw_input = file.read()
    lines = raw_input.splitlines()


# --- Part 1 --- #

def split_string(string: str):
    return string[:len(string) // 2], string[len(string) // 2:]


def get_priority(item: str):
    if item.islower():
        return ord(item) - 96
    return ord(item) - 64 + 26


rucksacks = [split_string(line) for line in lines]

duplicates = []
for compartment1, compartment2 in rucksacks:
    for item in compartment1:
        if item in compartment2:
            duplicates.append(item)
            break

badge_priorities = [get_priority(item) for item in duplicates]
print(sum(badge_priorities))

# --- Part 2 --- #

badges = []
combined_rucksacks = [comp1 + comp2 for comp1, comp2 in rucksacks]
for i in range(0, len(combined_rucksacks), 3):
    for item in combined_rucksacks[i]:
        if item in combined_rucksacks[i + 1] and item in combined_rucksacks[i + 2]:
            badges.append(item)
            break

badge_priorities = [get_priority(item) for item in badges]
print(sum(badge_priorities))
