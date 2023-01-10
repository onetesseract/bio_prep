from collections import defaultdict

# "1w", "2w", etc, "1b", "2b", "n"
board = defaultdict(lambda: -1)

# initialise default board
y = 4
y1 = 0
for x in range(5):
    board[(x, y)] = str(x + 1) + "b"
    board[(x, y1)] = str(x + 1) + "w"
    for _y in range(1, 4):
        board[(x, _y)] = 0

board[(2, 2)] = "n"

def print_board():
    for y in range(4, -1, -1):
        for x in range(5):
            p = board[(x, y)]
            if p == 0:
                print(".", end="")
            elif p == "n":
                print("*", end="")
            elif p.endswith("w"):
                print("F", end="")
            elif p.endswith("b"):
                print("S", end="")
        print()
    print()
    
# print_board()

def is_board_win(lboard):
    y = 4
    y1 = 0
    for x in range(5):
        if lboard[(x, y)] == "n":
            return "b"
        if lboard[(x, y1)] == "n":
            return "w"
    return False

def dir_pos(pos, dir):
    x, y = pos
    if dir == 1:
        # up
        y += 1
    if dir == 2:
        # up right
        y += 1
        x += 1
    if dir == 3:
        x += 1
    if dir == 4:
        y -= 1
        x += 1
    if dir == 5:
        y -= 1
    if dir == 6:
        y -= 1
        x -= 1
    if dir == 7:
        x -=1
    if dir == 8:
        x -= 1
        y += 1
    return (x, y)

def can_piece_move_in_dir(lboard, pos, dir):
    new_pos = dir_pos(pos, dir)
    return lboard[new_pos] == 0

def can_piece_move_at_all(lboard, pos):
    for dir in range(1, 9):
        if can_piece_move_in_dir(lboard, pos, dir): return True
    return False

def move_piece(lboard, _pos, dir):
    global board
    # if lboard == board:
        # print("Moving", _pos, board[(_pos)], dir)
    pos = _pos
    if not can_piece_move_in_dir(lboard, pos, dir): print("BAD BAD BAD")
    pos = dir_pos(pos, dir)
    while lboard[dir_pos(pos, dir)] == 0:
        pos = dir_pos(pos, dir)
    lboard[pos] = lboard[_pos]
    lboard[_pos] = 0
    return lboard

def find_piece(lboard, piece):
    for (k, v) in lboard.items():
        if v == piece: return k
    print("BAD BAD", piece)

def strat(player, _piece):
    global board
    neutron = find_piece(board, "n")
    piece = find_piece(board, _piece)
    do_all_moves_lose = True
    moves_moving_my_piece = []
    for dir in range(1, 9):
        # print("trying", dir)
        if can_piece_move_in_dir(board, neutron, dir):
            # print(dir, "can move")
            lboard = board.copy()
            lboard = move_piece(lboard, neutron, dir)
            win = is_board_win(lboard)
            if win == player:
                move_piece(board, neutron, dir)
                return
            if win == False:
                do_all_moves_lose = False
            else:
                continue
            can_my_piece_move = can_piece_move_at_all(lboard, piece)
            if can_my_piece_move:
                moves_moving_my_piece.append(dir)
    if do_all_moves_lose:
        # ah well
        for dir in range(1, 9):
            if can_piece_move_in_dir(board, neutron, dir):
                move_piece(board, neutron, dir)
                return
    # move it in the first dir where my piece can move
    board = move_piece(board, neutron, moves_moving_my_piece[0])
    for dir in range(1, 9):
        if can_piece_move_in_dir(board, piece, dir):
            board = move_piece(board, piece, dir)
            return

if __name__ == "__main__":
    w_order = [int(i) for i in input().strip().split()]
    b_order = [int(i) for i in input().strip().split()]

    move = 0

    strat("w", str(w_order[move % 5]) + "w") # len(w_order)
    print_board()
    strat("b", str(w_order[move % 5]) + "b")
    print_board()
    move += 1

    while is_board_win(board) == False:
        strat("w", str(w_order[move % 5]) + "w") # len(w_order)
        if is_board_win(board) != False:
            break
        strat("b", str(w_order[move % 5]) + "b")
        move += 1

    print_board()