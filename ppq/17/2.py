from math import floor
from collections import defaultdict

class Vertex:
    up = False
    down = False
    right = False
    left = False

# edges up clockwise through left
vertices = [Vertex() for i in range(36)]
boxes = [0 for i in range(25)]
score = defaultdict(lambda: 0)

def try_add_edge_to_point(point):
    valid = False
    direction = -1
    while point <= 35:
        v = vertices[point]
        if not v.up and point > 5:
            # its not top row or up
            v.up = True
            direction = 0
            vertices[point - 6].down = True
            break
        if not v.right and not (point + 1) % 6 == 0:
            # its not far right or right
            v.right = True
            direction = 1
            vertices[point + 1].left = True
            break
        if not v.down and point < 30:
            # down and not bottom row
            v.down = True
            direction = 2
            vertices[point + 6].up = True
            break
        if not v.left and not (point % 6) == 0:
            # left and not left edge
            v.left = True
            direction = 3
            vertices[point - 1].right = True
            break
        point += 1
    
    if point == 36: return (False, -1, direction)
    else:
        return (True, point, direction)

def would_line_make_box(point, direction):
    if point < 0 or point > 35: return []
    out = []
    if direction == 0:
        # up
        if (point > 5 and (point + 1) % 6 != 0 and vertices[point - 6].right and vertices[point - 6 + 1].down and vertices[point + 1].left):
            out.append((True, (point-6) % 6, floor((point - 6) / 6)))
        if (point > 6 and point % 6 != 0 and vertices[point - 6].left and vertices[point - 6 - 1].down and vertices[point - 1].right):
            out.append((True, (point-6-1) % 6, floor((point-6-1) / 6)))
    if direction == 1:
        # right
        if (point < 30 and (point + 1) % 6 != 0 and vertices[point + 1].down and vertices[point + 6 + 1].left and vertices[point + 6].up):
            out.append((True, point%6, floor(point/6)))
        elif (point > 5 and (point + 1) % 6 != 0 and vertices[point + 1].up and vertices[point + 1 -6].left and vertices[point - 6].down):
            out.append((True, (point - 6) % 6, floor((point - 6)/6)))
    if direction == 2:
        # down
        return would_line_make_box(point + 6, 0)
    if direction == 3:
        # left
        if (point % 6) == 0:
            return []
        else:
            return would_line_make_box(point - 1, 1)
    print("out", out)
    return out

def apply_move(player, point):
    success, point, direction = try_add_edge_to_point(point)
    print(point, direction)
    if not success: exit(1)
    scores = would_line_make_box(point, direction)
    for (_, x, y) in scores:
        boxes[y * 5 + x] = player
        score[player] = score[player] + 1

def print_board():
    for i in range(25):
        if boxes[i] == 1:
            print("X", end="")
        elif boxes[i] == 2:
            print("O", end="")
        else:
            print("*", end="")
        if (i + 1) % 5 == 0:
            print("")

def main():
    p1_pos, p1_mod, p2_pos, p2_mod, moves = [int(i) for i in input().strip().split(" ")]
    for i in range(moves):
        if i % 2 == 0:
            print("P1 moving")
            #p1:
            p1_pos += p1_mod
            p1_pos = p1_pos % 36
            apply_move(1, p1_pos)
        else:
            print("P2 moving")
            #p2
            p2_pos += p2_mod
            p2_pos = p2_pos % 36
            apply_move(2, p2_pos)
    
    print_board()
    print(score[1], score[2])

if __name__ == "__main__":
    main()