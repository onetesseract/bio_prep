from collections import defaultdict
from math import floor

world = defaultdict(lambda: 0)

# TODO: weird reflection?

def handle_migrations():
    while max(world.values()) >= 4:
        for ((x, y), v) in list(world.items()):
            if v >= 4:
                world[(x, y)] -= 4
                world[(x + 1, y)] += 1
                world[(x - 1, y)] += 1
                world[(x, y + 1)] += 1
                world[(x, y - 1)] += 1

def print_world():
    for y in range(2, -3, -1):
        for x in range(-2, 3):
            print(world[(x, y)], end=" ")
        print()

def add_person(pos, seq, moves):
    # print(pos, seq, moves)
    offset = seq[moves % len(seq)]
    pos += offset
    pos %= 25
    y_loc = floor(pos / 5)
    x_loc = pos % 5
    y_loc = 2 - y_loc
    x_loc -= 2
    # print("Pos is", x_loc, y_loc, pos)
    world[(x_loc, y_loc)] += 1

    return pos

def main():
    p, _, n = [int(i) for i in input().strip().split(" ")]
    seq = [int(i) for i in input().strip().split(" ")]
    pos = p - 1
    for move in range(n):
        pos = add_person(pos, seq, move)
        handle_migrations()
    
    print_world()

if __name__ == "__main__":
    main()