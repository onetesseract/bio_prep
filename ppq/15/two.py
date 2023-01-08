from collections import defaultdict
from math import floor

_board = defaultdict(lambda: False)

def is_placement_valid(board, x, y):
    for y_offset in range(-1, 2):
        for x_offset in range(-1, 2):
            if board[(x + x_offset, y + y_offset)]:
                return False

    return True

def place_n_ship(board, ships, n, a, c, m, r):
    while True:
        r = (a * r + c) % m
        y = floor((r%100)/10)
        x = r%10
        r = (a * r + c) % m
        if r % 2 == 0:
            # horizontal
            if x + n - 1 > 9:
                continue # out of bounds
            valid = True
            for i in range(x, x + n):
                if not is_placement_valid(board, i, y):
                    valid = False
                    break
            
            if not valid:
                continue

            # valid
            for i in range(x, x + n):
                board[(i, y)] = True
            ships.append(((x, y), "H"))
            break
        else:
            # vertical
            if y + n - 1 > 9:
                continue # out of bounds
            valid = True
            for i in range(y, y + n):
                if not is_placement_valid(board, x, i):
                    valid = False
                    break
            
            if not valid:
                continue

            # valid
            for i in range(y, y + n):
                board[(x, i)] = True
            ships.append(((x, y), "V"))
            break
    
    return r

def main(a, c, m):
    r = 0
    board = defaultdict(lambda: False)
    ships = []
    for freq, n in [(1, 4), (2, 3), (3, 2), (4, 1)]:
        for i in range(freq):
            r = place_n_ship(board, ships, n, a, c, m, r)
    
    for (x, y), dir in ships:
        print(x, y, dir)
    
a, c, m = [int(i) for i in input().strip().split(" ")]
main(a, c, m)
    


