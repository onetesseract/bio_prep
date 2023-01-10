from string import ascii_lowercase
from string import ascii_uppercase

from collections import defaultdict, deque

# 0= off, 1= dim, 2= on, mod 3

def string_to_board(s):
    out = [0 for i in range(25)]
    for i in s:
        if i.islower():
            out[ascii_lowercase.index(i)] = 1
        else:
            out[ascii_uppercase.index(i)] = 2
    
    return out



def press_button(_board, index):
    board = _board.copy()
    do_up = True
    do_down = True
    do_left = True
    do_right = True
    if index < 5: do_up = False
    if index >= 20: do_down = False
    if index % 5 == 0: do_left = False
    if (index + 1) % 5 == 0: do_right = False
    board[index] += 1
    board[index] %= 3
    if do_up:
        board[index - 5] += 1
        board[index - 5] %= 3
    if do_down:
        board[index + 5] += 1
        board[index + 5] %= 3
    if do_left:
        board[index - 1] += 1
        board[index - 1] %= 3
    if do_right:
        board[index + 1] += 1
        board[index + 1] %= 3
    
    return board

# press buttons lol
def push_my_buttons(board):
    # print(board)
    buttons = []
    for i in range(5, len(board)):
        while board[i - 5] != 0:
            board = press_button(board, i)
            buttons.append(i)
    if 1 in board or 2 in board:
        print(board)
        return "IMPOSSIBLE"
    else:
        out = []
        i = 0
        while i != len(buttons):
            if buttons[i + 1] == buttons[i]:
                out.append(ascii_uppercase[buttons[i]])
                i += 1
            else:
                out.append(ascii_lowercase[buttons[i]])
            i += 1
        return "".join(out)

def permutations_of(board):
    out = []
    for i in range(25):
        out.append(press_button(board, i))
    
    return out

def search(board):
    prev = {}
    already_visited = set()
    to_visit = deque()
    _presses = [0 for i in range(25)]
    to_visit.append((board, _presses))

    while len(to_visit) != 0:
        state, presses = to_visit.popleft()
        # print("Trying", state)
        if tuple(state) in already_visited: continue
        already_visited.add(tuple(state))
        for button in range(25):
            if presses[button] == 2: continue
            new_state = press_button(state, button)
            if tuple(new_state) in already_visited: continue
            prev[tuple(new_state)] = (button, state)
            if not 1 in new_state and not 2 in new_state: # win!
                to_visit = []
                break
            new_presses = presses.copy()
            new_presses[button] += 1
            to_visit.append((new_state, new_presses))
    
    # back-search
    t = [0 for i in range(25)]
    series = []
    while t != board:
        button, t = prev[tuple(t)]
        if t in prev and prev[tuple(t)][0] == button:
            _, t = prev[tuple(t)]
            series.append(ascii_uppercase[button])
        else:
            series.append(ascii_lowercase[button])
    
    return "".join(reversed(series))
    
print(push_my_buttons(string_to_board(input().strip())))