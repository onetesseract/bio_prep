def choose_letter(a, b):
    if a == b: return a
    if a == 'R':
        if b == 'G': return 'B'
        if b == 'B': return 'G'
    if a == 'G':
        if b == 'R': return 'B'
        if b == 'B': return 'R'
    if a == 'B':
        if b == 'R': return 'G'
        if b == 'G': return 'R'

def solve(starting_pos):
    old_line = starting_pos
    next_line = []
    while len(old_line) != 1:
        for i in range(len(old_line) - 1):
            next_line.append(choose_letter(old_line[i], old_line[i + 1]))

        old_line = next_line
        next_line = []

    return old_line[0]

print(solve(list(input().strip())))