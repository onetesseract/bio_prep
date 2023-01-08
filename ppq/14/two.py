matrix = []
n = 0

def right_of(pos):
    x, y = pos
    return (x + 1, y)
def left_of(pos):
    x, y = pos
    return (x - 1, y)
def top_of(pos):
    x, y = pos
    return (x, y + 1)
def bottom_of(pos):
    x, y = pos
    return (x, y - 1)


def chase_red_line(prev, pos):
    global matrix
    global n
    x, y = pos
    if x < 0 or x >= n or y < 0 or y >= n:
        return (0, prev)
    if pos in prev: # loop yes!
        return (len(prev), prev)
    
    number = matrix[x][y]
    
    if len(prev) == 0:
        if number in [1, 3, 4]:
            # we can go up
            return chase_red_line(prev + [(x, y)], top_of(pos))
        elif number in [5, 6]:
            # go down
            return chase_red_line(prev + [(x, y)], top_of(pos)) 
        elif number == 2:
            # go right
            return chase_red_line(prev + [(x, y)], right_of(pos))
    
    prev_pos = prev[-1]
    

    if number == 1:
        # straight up
        if prev_pos == top_of(pos):
            # go down
            return chase_red_line(prev + [(x, y)], bottom_of(pos))
        if prev_pos == bottom_of(pos):
            # go up
            return chase_red_line(prev + [(x, y)], top_of(pos))
        else:
            return (0, prev)
    if number == 2:
        # straight across
        if prev_pos == right_of(pos):
            # go leeeft
            return chase_red_line(prev + [(x, y)], left_of(pos))
        if prev_pos == left_of(pos):
            # go right
            return chase_red_line(prev + [(x, y)], right_of(pos))
        else:
            return (0, prev)
    if number == 3:
        # left to top
        if prev_pos == left_of(pos):
            # from the left, go top
            return chase_red_line(prev + [(x, y)], top_of(pos))
        if prev_pos == top_of(pos):
            # go left
            return chase_red_line(prev + [(x, y)], left_of(pos))
        else:
            return (0, prev)
    if number == 4:
        # top to right
        if prev_pos == top_of(pos):
            # right
            return chase_red_line(prev + [(x, y)], right_of(pos))
        if prev_pos == right_of(pos):
            # top
            return chase_red_line(prev + [(x, y)], top_of(pos))
        else:
            return (0, prev)
    if number == 5:
        # right to bottom
        if prev_pos == right_of(pos):
            # bottom
            return chase_red_line(prev + [(x, y)], bottom_of(pos))
        if prev_pos == bottom_of(pos):
            # right
            return chase_red_line(prev + [(x, y)], right_of(pos))
        else:
            return (0, prev)
    if number == 6:
        # bottom to left
        if prev_pos == bottom_of(pos):
            # right
            return chase_red_line(prev + [(x, y)], left_of(pos))
        if prev_pos == left_of(pos):
            # top
            return chase_red_line(prev + [(x, y)], bottom_of(pos))
        else:
            return (0, prev)

def chase_green_line(prev, pos):
    global matrix
    global n
    x, y = pos
    if x < 0 or x >= n or y < 0 or y >= n:
        return (0, prev)
    if pos in prev: # loop yes!
        return (len(prev), prev)
    
    number = matrix[x][y]
    
    if len(prev) == 0:
        if number in [2, 5, 6]:
            # we can go up
            return chase_green_line(prev + [(x, y)], top_of(pos))
        elif number in [3, 4]:
            # go down
            return chase_green_line(prev + [(x, y)], bottom_of(pos)) 
        elif number == 1:
            # go right
            return chase_green_line(prev + [(x, y)], right_of(pos))
    
    prev_pos = prev[-1]
    

    if number == 2:
        # straight up
        if prev_pos == top_of(pos):
            # go down
            return chase_green_line(prev + [(x, y)], bottom_of(pos))
        if prev_pos == bottom_of(pos):
            # go up
            return chase_green_line(prev + [(x, y)], top_of(pos))
        else:
            return (0, prev)
    if number == 1:
        # straight across
        if prev_pos == right_of(pos):
            # go leeeft
            return chase_green_line(prev + [(x, y)], left_of(pos))
        if prev_pos == left_of(pos):
            # go right
            return chase_green_line(prev + [(x, y)], right_of(pos))
        else:
            return (0, prev)
    if number == 5:
        # left to top
        if prev_pos == left_of(pos):
            # from the left, go top
            return chase_green_line(prev + [(x, y)], top_of(pos))
        if prev_pos == top_of(pos):
            # go left
            return chase_green_line(prev + [(x, y)], left_of(pos))
        else:
            return (0, prev)
    if number == 6:
        # top to right
        if prev_pos == top_of(pos):
            # right
            return chase_green_line(prev + [(x, y)], right_of(pos))
        if prev_pos == right_of(pos):
            # top
            return chase_green_line(prev + [(x, y)], top_of(pos))
        else:
            return (0, prev)
    if number == 3:
        # right to bottom
        if prev_pos == right_of(pos):
            # bottom
            return chase_green_line(prev + [(x, y)], bottom_of(pos))
        if prev_pos == bottom_of(pos):
            # right
            return chase_green_line(prev + [(x, y)], right_of(pos))
        else:
            return (0, prev)
    if number == 4:
        # bottom to left
        if prev_pos == bottom_of(pos):
            # right
            return chase_green_line(prev + [(x, y)], left_of(pos))
        if prev_pos == left_of(pos):
            # top
            return chase_green_line(prev + [(x, y)], bottom_of(pos))
        else:
            return (0, prev)

def construct_matrix():
    global matrix
    global n
    n = int(input().strip())
    matrix = [[0 for i in range(n)] for i in range(n)]
    for y in range(n - 1, -1, -1):
        inpt = [int(i) for i in input().strip().split(" ")]
        for x in range(len(inpt)):
            matrix[x][y] = inpt[x]

def ask():
    construct_matrix()

    red = 0
    to_ask = []
    for y in range(n):
        for x in range(n):
            to_ask.append((x, y))
    visited = []
    for pos in to_ask:
        if pos in visited:
            continue
        score, prev = chase_red_line([], pos)
        if score != 0:
            red += score
            visited += prev
    green = 0
    visited = []
    for pos in to_ask:
        if pos in visited:
            continue
        score, prev = chase_green_line([], pos)
        if score != 0:
            green += score
            visited += prev
    print(red, green)
        
ask()