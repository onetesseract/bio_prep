hlines = [(0, 0) for i in range(6*6)]
vlines = [(0, 0) for i in range(6*5)]

import sys
sys.setrecursionlimit(1 << 10)

# squares = [0 for i in range(5*5)]



def try_link_point(point_index, player, move_index):
    point_index = point_index % 36
    # up first
    if not point_index < 6: # no can do if else
        if vlines[point_index - 6] == (0, 0):
            vlines[point_index - 6] = (player, move_index)
            return point_index
    # then right
    if not point_index % 6 == 5: # on right edge of grid
        if hlines[point_index] == (0, 0):
            hlines[point_index] = (player, move_index)
            return point_index
    # then down
    if not point_index > 29: # bottom row
        if vlines[point_index] == (0, 0):
            vlines[point_index] = (player, move_index)
            return point_index
    # then left!
    if not point_index % 6 == 0: # left edge
        if hlines[point_index - 1] == (0, 0):
            hlines[point_index - 1] = (player, move_index)
            return point_index
    return try_link_point(point_index + 1, player, move_index)

def is_box_won(box_index):
    # we need to +1 to all above 5, +2 to all above 10, +3 to all above 15, ..., +4 to all above 20 until 25
    if box_index >= 20:
        box_index += 4
    elif box_index >= 15:
        box_index += 3
    elif box_index >= 10:
        box_index += 2
    elif box_index >= 5:
        box_index += 1
    # lines would be uhh for point uhh
    # above is hlines[index]
    # below is hlines[index + 5]
    # left is vlines[index]
    # right is vlines[index + 1]
    # player, turn etc etc
    (ap, at) = hlines[box_index]
    (bp, bt) = hlines[box_index + 5]
    (cp, ct) = vlines[box_index]
    (dp, dt) = vlines[box_index + 1]

    if 0 in [ap, bp, cp, dp]: return 0
    mx = max(at, bt, ct, dt)
    if at == mx: return ap
    if bt == mx: return bp
    if ct == mx: return cp
    if dt == mx: return dp

    print("gone badly")

def print_board():
    p1_count = 0
    p2_count = 0
    for i in range(25):
        if i % 5 == 0:
            print()
        owner = is_box_won(i)
        if owner not in [0, 1, 2]:
            print(owner)
        if owner == 1:
            print("x", end="")
            p1_count += 1
        if owner == 2:
            print("o", end="")
            p2_count += 1
        if owner == 0:
            print("*", end="")
    print()
    print(p1_count, p2_count)

def play(p1, m1, p2, m2, moves):
    is_p1_turn = True
    for i in range(moves):
        if is_p1_turn:
            p1 += m1
            p1 = try_link_point(p1, 1, i)
        else:
            p2 += m2
            p2 = try_link_point(p2, 2, i)
        is_p1_turn = not is_p1_turn
    
    print_board()

p1, m1, p2, m2, moves = [int(i) for i in input().strip().split(" ")]
play(p1, m1, p2, m2, moves)


