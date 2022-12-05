# https://adventofcode.com/2022/day/5

with open('input.txt', 'r') as file:
    raw_input = file.read()


# --- Part 1 --- #
def parse_stacks(stacks_string):
    stack_lines = stacks_string.splitlines()
    stacks_dict = dict()

    for line in stack_lines[:-1]:
        for i in range(1, len(line), 4):
            stack_index = i // 4 + 1
            if line[i].isalnum():
                if not stack_index in stacks_dict:
                    stacks_dict[stack_index] = []
                stacks_dict[stack_index].append(line[i])

    for key in stacks_dict:
        stacks_dict[key].reverse()
    return stacks_dict


def parse_instructions(instructions_string):
    return [parse_instruction(line) for line in instructions_string.splitlines()]


def parse_instruction(instruction_string):
    return tuple(int(instruction_string.split(' ')[i]) for i in [1, 3, 5])


stacks_input, instructions_input = raw_input.split('\n\n')
instructions = parse_instructions(instructions_input)
stacks = parse_stacks(stacks_input)

for instruction in instructions:
    amount, from_stack, to_stack = instruction

    for _ in range(amount):
        item = stacks[from_stack].pop()
        stacks[to_stack].append(item)

for stack_index in range(1, 10):
    print(stacks[stack_index][-1], end='')

# --- Part 2 --- #
stacks = parse_stacks(stacks_input)

for instruction in instructions:
    amount, from_stack, to_stack = instruction

    stacks[to_stack] += stacks[from_stack][-amount:]
    stacks[from_stack] = stacks[from_stack][:-amount]

print()
for stack_index in range(1, 10):
    print(stacks[stack_index][-1], end='')
