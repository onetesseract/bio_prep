die_state = [3, 6,
                5]

def roll_up(_state):
    state = _state.copy()
    l, b, d = state
    _d = d
    d = b
    b = 7 - _d

    state = [l, b, d]
    return state

def roll_down(_state):
    state = _state.copy()
    l, b, d = state
    _b = b
    b = d
    d = 7 - _b

    state = [l, b, d]
    return state

def roll_left(_state):
    state = _state.copy()
    l, b, d = state
    _b = b
    b = l
    l = 7 - _b

    state = [l, b, d]
    return state

def roll_right(_state):
    state = _state.copy()
    l, b, d = state
    _l = l
    l = b
    b = 7 - _l

    state = [l, b, d]
    return state

# center is 5, 5

heading = "U" # U, L, R, or D

def opposite_heading(head):
    return {"U": "D", "L": "R", "R": "L", "D": "U"}[head]

def rot_clockwise(head):
    return {"U": "R", "R": "D", "D": "L", "L": "U"}[head]

def rot_acw(head):
    return {"U": "L", "L": "D", "D": "R", "R": "U"}[head]

def move_with_heading(x, y, head):
    if head == "U": return (x, y + 1)
    if head == "D": return (x, y - 1)
    if head == "L": return (x - 1, y)
    if head == "R": return (x + 1, y)

def roll_heading(head, state):
    if head == "U": return roll_up(state)
    if head == "D": return roll_down(state)
    if head == "L": return roll_left(state)
    if head == "R": return roll_right(state)

def move(pos, _head, state):
    head = _head
    x, y = pos
    l, b, d = state
    top = 7 - b
    
    x, y = move_with_heading(x, y, head)

    x = x % 11
    y = y % 11

    new_state = roll_heading(head, state)
    
    return ((x, y),  new_state)

def print_grid_area(pos, grid):
    x, y = pos
    for y_offset in [1, 0, -1]:
        _y = y + y_offset
        for x_offset in [-1, 0, 1]:
            _x = x + x_offset
            if _x < 0 or _x > 10 or _y < 0 or _y > 10:
                print("x", end="")
            else:
                print(grid[_x][_y], end="")
        print()

q = ["U", "D", "L", "R"]

def bytearray_to_four_headings(num):
    e = (0b110000000000 & num) >> 10
    f = (0b1100000000 & num) >> 8
    a = (0b11000000 & num) >> 6
    b = (0b00110000 & num) >> 4
    c = (0b00001100 & num) >> 2
    d = (0b00000011 & num)

    return [q[e], q[f], q[a], q[b], q[c], q[d]]


def four_seq():
    
    k = 0
    tot = 0
    # max is four/2 bytes, or 2 bytes, or like 65535
    while k <= 0b111111111111:
        headings = bytearray_to_four_headings(k)
        tot += main2(headings)
        k += 1

    print(tot)



def main2(headings):
    pos = (5, 5)
    state = die_state

    # print_grid_area(pos, grid)

    for k in range(6):
        n = 1
        head = headings[k]
        # for i in range(n):
        pos, state = move(pos, head, state)
            
    l, d, b = state
    if pos == (5, 5) and not d == 6:
        return 1
    else:
        return 0

if __name__ == "__main__":
    four_seq()

