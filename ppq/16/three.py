from math import log2, floor, ceil
from collections import defaultdict, deque
from functools import lru_cache

@lru_cache(maxsize=None)
def is_prime(n):
    # print("Trying to see if", n, "is prime")
    for i in range(2, ceil(n**0.5 + 1)):
        if i%n == 0:
            return False
    return True

@lru_cache(maxsize=None)
def try_permutations(p, pow_lim, lim):
    out = []
    for i in range(1, pow_lim + 1):
        q = 2**i
        if p > q and is_prime(p - q):
            out.append(p - q)
        if p + q <= lim and is_prime(p + q):
            out.append(p + q)
    # print(out)
    return out
    
def solve(a, b, lim):
    pow_lim = floor(log2(lim))
    print("Pow-lim", pow_lim)
    # lets try a double-ended bfs
    a_distances = defaultdict(lambda: (999999999, []))
    b_distances = defaultdict(lambda: (999999999, []))
    a_search = deque()
    a_search.append((a, 0, [a]))
    b_search = deque()
    b_search.append((b, 0, [b]))
    while len(a_search) != 0 or len(b_search) != 0:
        a_, dist, path = a_search.popleft()
        # print("Now trying:", a_)
        for i in try_permutations(a_, pow_lim, lim):
            if i in b_distances.keys():
                # path found!!
                # print(path + [i], b_distances[i])
                return dist + 1 + b_distances[i][0]
            if a_distances[i][0] > dist + 1:
                a_distances[i] = (dist + 1, path + [i])
                a_search.append((i, dist + 1, path + [i]))
        
        b_, dist, path = b_search.popleft()
        for i in try_permutations(b_, pow_lim, lim):
            if i in a_distances.keys():
                # path found!!
                # print(path + [i], a_distances[i])
                return dist + 1 + a_distances[i][0]
            if b_distances[i][0] > dist + 1:
                b_distances[i] = (dist + 1, path + [i])
                b_search.append((i, dist + 1, path + [i]))
    
    return "No path"

max, p, q = [int(i) for i in input().strip().split(" ")]
print(solve(p, q, max))