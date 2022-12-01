# https://adventofcode.com/2022/day/1

with open('input.txt', 'r') as file:
    input = file.read()

# --- Part 1 --- #
input_per_elf = input.split('\n\n')

calories_per_elf = [[int(calorie) for calorie in input_of_elf.split('\n')] for input_of_elf in input_per_elf]

sum_per_elf = [sum(calories) for calories in calories_per_elf]
print(max(sum_per_elf))

# --- Part 2 --- #
highest_3_sums = sorted(sum_per_elf, reverse=True)[:3]
print(sum(highest_3_sums))
