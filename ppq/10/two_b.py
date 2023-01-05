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

def move(pos, _head, grid, state):
    head = _head
    x, y = pos
    l, b, d = state
    top = 7 - b
    num = grid[x][y]
    grid[x][y] = ((num + top - 1) % 6) + 1

    if grid[x][y] == 1 or grid[x][y] == 6:
        pass
    elif grid[x][y] == 2:
        head = rot_clockwise(head)
    elif grid[x][y] == 3 or grid[x][y] == 4:
        head = opposite_heading(head)
    elif grid[x][y] == 5:
        head = rot_acw(head)
    
    x, y = move_with_heading(x, y, head)

    x = x % 11
    y = y % 11

    new_state = roll_heading(head, state)
    
    return ((x, y), head, grid, new_state)

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

def possibilities():
    q = [0, 0, 0, 0, 0, 0, 0]
    out = []

    while q[0] != 1:
        i = 6
        q[i] += 1
        while True:
            if q[i] == 7:
                q[i] == 1
                q[i - 1] += 1
            else: break
        out.append(q[1:])
    
    return out

def main():
    pos = (5, 5)
    state = die_state
    head = "U"

    grid = [1 for i in range(11)]
    grid = [grid.copy() for i in range(11)]

    grid[4][6], grid[5][6], grid[6][6] = [int(i) for i in input().strip().split(" ")]
    grid[4][5], grid[5][5], grid[6][5] = [int(i) for i in input().strip().split(" ")]
    grid[4][4], grid[5][4], grid[6][4] = [int(i) for i in input().strip().split(" ")]

    # print_grid_area(pos, grid)

    # damn permutations

    while True:
        n = int(input())
        if n == 0: exit(0)
        for i in range(n):
            pos, head, grid, state = move(pos, head, grid, state)

        print_grid_area(pos, grid)
        print(pos)
        # print(grid)

if __name__ == "__main__":
    main()

