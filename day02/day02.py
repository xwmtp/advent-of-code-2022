# https://adventofcode.com/2022/day/2

with open('input.txt', 'r') as file:
    raw_input = file.read()
    lines = raw_input.splitlines()

rounds = [line.split(' ') for line in lines]

# --- Part 1 --- #

points = {
    'X': 1,  # rock
    'Y': 2,  # paper
    'Z': 3,  # scissors
}


def p2_score(p1, p2):
    if (p1 == 'A' and p2 == 'X') or (p1 == 'B' and p2 == 'Y') or (p1 == 'C' and p2 == 'Z'):  # draw
        return 3
    if p1 == 'A':  # rock
        return 0 if p2 == 'Z' else 6
    if p1 == 'B':  # paper
        return 0 if p2 == 'X' else 6
    if p1 == 'C':  # scissors
        return 0 if p2 == 'Y' else 6


total_score = 0
for p1_play, p2_play in rounds:
    total_score += p2_score(p1_play, p2_play) + points[p2_play]
print(total_score)


# --- Part 2 --- #

def get_score_of_p2_result(p1, p2_result):
    if p2_result == 'X':  # lose
        if p1 == 'A':
            return points['Z'] + 0
        if p1 == 'B':
            return points['X'] + 0
        if p1 == 'C':
            return points['Y'] + 0
    if p2_result == 'Y':  # draw
        if p1 == 'A':
            return points['X'] + 3
        if p1 == 'B':
            return points['Y'] + 3
        if p1 == 'C':
            return points['Z'] + 3
    if p2_result == 'Z':  # win
        if p1 == 'A':
            return points['Y'] + 6
        if p1 == 'B':
            return points['Z'] + 6
        if p1 == 'C':
            return points['X'] + 6


total_score = 0
for p1_play, p2_result in rounds:
    total_score += get_score_of_p2_result(p1_play, p2_result)
print(total_score)
