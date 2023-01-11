from collections import defaultdict

box = defaultdict(lambda: '.')

# dir: 0, 1, 2, 3

def exit_coord_to_side(x, y):
    if x == 0: # out the left
        return "L " + str(y)
    if x == 11: # out the right
        return "R " + str(y)
    if y == 0: # fell off
        return "B " + str(x)
    if y == 11:
        return "T " + str(x)
    
def side_to_coord_dir(side):
    edge, pos = side.split(" ")
    pos = int(pos)
    if edge == "L":
        dir = 1
        x = 1
        y = pos
    if edge == "R":
        dir = 3
        x = 10
        y = pos
    if edge == "T":
        dir = 2
        x = pos
        y = 10
    if edge == "B":
        dir = 0
        x = pos
        y = 1
    return (x, y, dir)
        

def move_ray(_x, _y, _dir):
    global box
    x, y = _x, _y
    # print(x, y)
    dir = _dir
    dlx, dly, drx, dry = 0, 0, 0, 0
    shx, shy = 0, 0

    if dir == 0: #up
        dlx = x - 1
        dly = y + 1
        drx = x + 1
        dry = y + 1
        shx = x
        shy = y + 1
    if dir == 1: # right
        dlx = x + 1
        dly = y + 1
        drx = x + 1
        dry = y - 1
        shx = x + 1
        shy = y
    if dir == 2: # down
        dlx = x + 1
        dly = y - 1
        drx = x - 1
        dry = y - 1
        shx = x
        shy = y - 1
    if dir == 3: # left
        dlx = x - 1
        dly = y - 1
        drx = x - 1
        dry = y + 1
        shx = x - 1
        shy = y

    # square of interest is x, y

    box[(x, y)] = "+"

    if x < 1 or x > 10 or y < 1 or y > 10:
        # we outside the box
        return "Exits at " + exit_coord_to_side(x, y)
    if box[(shx, shy)] == 'A': # we hit an atom
        box[(shx, shy)] = "*"
        return "Absorbed"
    
    if box[(drx, dry)] == "A" and box[(dlx, dly)] == "A":
        # print(x, y, drx, dry, dlx, dly)
        return "Reflected"
    if box[(drx, dry)] == "A":
        # atom to the right
        # turn left, acw
        dir = (dir - 1) % 4
    if box[(dlx, dly)] == "A":
        dir = (dir + 1) % 4
    

    if dir == 0: #up
        y += 1
        dlx = x - 1
        dly = y + 1
        drx = x + 1
        dry = y + 1
    if dir == 1: # left
        x += 1
        dlx = x + 1
        dly = y + 1
        drx = x + 1
        dry = y - 1
    if dir == 2: # down
        y -= 1
        dlx = x + 1
        dly = y - 1
        drx = x - 1
        dry = y - 1
    if dir == 3: # right
        x -= 1
        dlx = x - 1
        dly = y - 1
        drx = x - 1
        dry = y - 1
    
    
    return move_ray(x, y, dir)

def init_box():
    global box
    for i in range(5):
        x, y = [int(i) for i in input().strip().split(" ")]
        box[(x, y)] = "A"

def print_box():
    global box
    for y in range(10, 0, -1):
        for x in range(1, 11):
            print(box[(x, y)], end="")
        print()

def main():
    global box
    init_box()
    _box = box.copy()
    print_box()
    i = input()
    while i != "X 0":
        x, y, dir = side_to_coord_dir(i)
        q = move_ray(x, y, dir)
        print_box()
        print(q)
        box = _box.copy()
        i = input()
    
main()

# b
"""
5
..........
.A........
..........
...A......
..........
.....A....
..........
.......A..
........A.
..........

c == 37

d:
No, it can't, for 3. Rays must be reversible, so it will cross every square either once, twice by reflection, twice by intersection, but never thrice because 
it would then align with itself, meaning it must have been reflected, so each square will be crossed an even number of times.
It can for four, here is an example

..A...A..
...+++...
.A.+.+...
..+X++...
.A.+..A..
   ^
Starting at the marked entry point, it crosses square X four times.
"""