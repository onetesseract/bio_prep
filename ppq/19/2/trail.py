from collections import defaultdict

world = defaultdict(lambda: -999999999)

# dirs are u r d l
#          0 1 2 3

def move_on_dir(_x, _y, dir):
    x = _x
    y = _y
    if dir == 0:
        y += 1
    if dir == 2: y -= 1
    if dir == 3: x -= 1
    if dir == 1: x += 1

    return (x, y)

def rot_cw(dir):
    return (dir + 1) % 4

def rot_acw(dir):
    return (dir - 1) % 4

decay, instructions, moves = input().strip().split(" ")
decay, moves = int(decay), int(moves)

tick = 0

x = 0
y = 0
dir = 0

for i in range(moves):
    # print("World looks like", world)
    # print("Start at", x, y, dir, tick)
    # print("inst", instructions[i % len(instructions)])
    # input()
    world[(x, y)] = tick
    if instructions[i % len(instructions)] == 'L':
        dir = rot_acw(dir)
    elif instructions[i % len(instructions)] == 'R':
        dir = rot_cw(dir)
    
    pos = move_on_dir(x, y, dir)
    if tick - world[pos] > (decay + 1):
        # valid to move
        x, y = pos
    else:
        valid = False
        for i in range(3):
            # print("Cannot move to", pos)
            dir = rot_cw(dir)
            pos = move_on_dir(x, y, dir)
            if world[pos] < tick - (decay - 1):
                # valid to move
                x, y = pos
                valid = True
                break
        
        if not valid:
            # oh no
            break
    
    tick += 1

print(f"({x},{y})")