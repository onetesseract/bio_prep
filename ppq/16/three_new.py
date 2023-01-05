from functools import lru_cache
import math
from collections import defaultdict, deque

from time import time_ns

@lru_cache(maxsize=None)
def is_prime(p):
    if p == 1: return False
    if p == 2: return True
    for i in range(2, math.ceil(p**0.5 + 1)):
        if p%i == 0: return False
    return True

@lru_cache(maxsize=None)
def choices_from(p, lim, loglim):
    out = []
    for q in range(0, loglim):
        i = pow(2, q)
        if p - i > 0 and is_prime(p - i):
            out.append(p - i)
        if p + i < lim and is_prime(p + i):
            out.append(p + i)
    # print("Options for", p, "are", out)
    return out

def dual_dj_search(a, b, lim):
    loglim = math.ceil(math.log2(lim))
    # visited_nodes = []
    a_shortest_paths = defaultdict(lambda: math.inf)
    a_shortest_paths[a] = 0
    # prev = {}
    a_to_visit = deque()
    a_to_visit.append((a, 0))
    
    b_shortest_paths = defaultdict(lambda: math.inf)
    b_shortest_paths[b] = 0
    # prev = {}
    b_to_visit = deque()
    b_to_visit.append((b, 0))
    both = [(a_shortest_paths, a_to_visit), (b_shortest_paths, b_to_visit)]
    switch = 0
    while len(both[switch][1]) != 0:
        shortest_paths, to_visit = both[switch]

        p, dist = to_visit.popleft()
        # print("Trying", p)
        for i in choices_from(p, lim, loglim):
            if i in both[1 - switch][0]:
                # path found!
                # print("Path!")
                return dist + 1 + 1 + both[1 - switch][0][i]
            if shortest_paths[i] > dist + 1:
                if shortest_paths[i] != math.inf: print("Broken")
                # prev[i] = p
                shortest_paths[i] = dist + 1
                to_visit.append((i, dist + 1))
        
        switch = 1 - switch
    
    # trace back
    # q = b
    # path = [b]
    # while q in prev.keys():
    #     q = prev[q]
    #     path.append(q)
    # print(path)
    return None # shortest_paths[b] + 1

def dj_search(a, b, lim):
    loglim = math.ceil(math.log2(lim))
    visited_nodes = []
    shortest_paths = defaultdict(lambda: math.inf)
    shortest_paths[a] = 0
    prev = {}
    to_visit = deque()
    to_visit.append((a, 0))
    while len(to_visit) != 0:
        p, dist = to_visit.popleft()
        # print("Trying", p)
        for i in choices_from(p, lim, loglim):
            if shortest_paths[i] > dist + 1:
                if shortest_paths[i] != math.inf: print("Broken")
                prev[i] = p
                shortest_paths[i] = dist + 1
                to_visit.append((i, dist + 1))
    
    # trace back
    # q = b
    # path = [b]
    # while q in prev.keys():
    #     q = prev[q]
    #     path.append(q)
    # print(path)
    return shortest_paths[b] + 1

def main():
    lim, a, b = [int(i) for i in input().strip().split(" ")]
    before = time_ns()
    print(dj_search(a, b, lim))
    after = time_ns()
    print("Conventional took", after - before, "ns")
    before = time_ns()
    print(dual_dj_search(a, b, lim))
    after = time_ns()
    print("New took", after - before, "ns")


main()