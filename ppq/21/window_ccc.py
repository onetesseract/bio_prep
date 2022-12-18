from collections import defaultdict, deque
distances = defaultdict(lambda: 99999999)

alpha = "ABCDEFGH"

def add(_window, _stack):
    window = _window
    window += _stack[0]
    stack = _stack[1:]
    return window, stack

def swap(_window, stack):
    window = list(_window)
    window[0], window[1] = window[1], window[0]
    return "".join(window), stack

def rotate(_window, stack):
    window = _window[1:]
    window += _window[0]
    return window, stack


def solve(target):
    window = ""
    stack = alpha[:len(target)]
    to_evaluate = deque()

    seqs = set()
    
    # distance from src, window, stack
    to_evaluate.append([0, window, stack, ""])
    while len(to_evaluate) != 0:
        dist, window, stack, seq = to_evaluate.popleft()
        if dist == 24 and window == target:
            seqs.add(seq)
        # print("Evaluating", dist, window, stack)
        if len(stack) != 0:
            new_window, new_stack = add(window, stack)
            if distances[new_window] >= (dist + 1):
                distances[new_window] = dist + 1
                # print("Add is better")
                to_evaluate.append([dist + 1, new_window, new_stack, seq + "a"])

        if len(window) > 1:
            new_window, new_stack = swap(window, stack)
            if distances[new_window] >= (dist + 1):
                distances[new_window] = dist + 1
                # print("Swap is better")
                to_evaluate.append([dist + 1, new_window, new_stack, seq + "s"])

            new_window, new_stack = rotate(window, stack)
            if distances[new_window] >= (dist + 1):
                distances[new_window] = dist + 1
                # print("Rotate is better")
                to_evaluate.append([dist + 1, new_window, new_stack, seq + "r"])
    
    print(seqs)
    print(len(seqs))
    return distances[target]

print(solve(input("")))

