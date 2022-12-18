from collections import defaultdict, deque
distances = defaultdict(lambda: False)

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

    total = 0
    dists = []
    
    # distance from src, window, stack
    to_evaluate.append([0, window, stack])
    while len(to_evaluate) != 0:
        dist, window, stack = to_evaluate.popleft()
        # print("Evaluating", dist, window, stack)
        if len(stack) != 0:
            new_window, new_stack = add(window, stack)
            if not (distances[new_window]):
                distances[new_window] = True
                # print("Add is better")
                if new_window == target:
                    total += 1
                    dists.append(dist + 1)
                    # continue
                to_evaluate.append([dist + 1, new_window, new_stack])

        if len(window) > 1:
            new_window, new_stack = swap(window, stack)
            if not distances[new_window]:
                distances[new_window] = True
                # print("Swap is better")
                if new_window == target:
                    total += 1
                    dists.append(dist + 1)
                    # continue
                to_evaluate.append([dist + 1, new_window, new_stack])

            new_window, new_stack = rotate(window, stack)
            if not distances[new_window]:
                distances[new_window] = True
                # print("Rotate is better")
                if new_window == target:
                    total += 1
                    dists.append(dist + 1)
                    # continue
                to_evaluate.append([dist + 1, new_window, new_stack])

    return total, dists

print(solve(input("")))
