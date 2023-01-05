from collections import defaultdict, deque

def does_fit(a, b, inbi):
    a, b = sorted([a, b])
    return a < inbi and b > inbi

def swap_to(_src, i, j):
    dest = _src.copy()
    dest[i] = _src[j]
    dest[j] = _src[i]
    return dest

def can_transform_into(src):
    if len(src) < 2: return []
    out = []
    for i in range(len(src) - 1): # two adj
        if i == 0:
            # special case
            if does_fit(src[i], src[i + 1], src[i + 2]):
                out.append(swap_to(src, i, i + 1))
        elif i == len(src) - 2:
            if does_fit(src[i], src[i + 1], src[i - 1]):
                out.append(swap_to(src, i, i + 1))
        else:
            if does_fit(src[i], src[i + 1], src[i - 1]):
                out.append(swap_to(src, i, i + 1))
            elif does_fit(src[i], src[i + 1], src[i + 2]):
                out.append(swap_to(src, i, i + 1))
    
    return out

def solve(initial):
    # distance, state
    queue = deque()
    queue.append((0, initial))
    distances = {}

    while len(queue) != 0:
        dist, state = queue.popleft()
        for i in can_transform_into(state):
            # i is a list, unhashable
            tup = tuple(i)
            if tup not in distances or distances[tup] > dist + 1:
                # better path found
                distances[tup] = dist + 1
                queue.append((dist + 1, i))
    
    return max(distances.values())

def solve2(initial):
    # distance, state
    queue = deque()
    queue.append((0, initial))
    distances = {}

    while len(queue) != 0:
        dist, state = queue.popleft()
        for i in can_transform_into(state):
            # i is a list, unhashable
            tup = tuple(i)
            if tup not in distances or distances[tup] > dist + 1:
                # better path found
                distances[tup] = dist + 1
                queue.append((dist + 1, i))
    print(distances.keys())
    return max([solve(list(i)) for i in distances.keys()])

def main():
    _ = input()
    start = input().strip()
    print(solve2(list(start)))

if __name__ == "__main__":
    main()