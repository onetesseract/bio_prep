digits = [ "ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
from functools import lru_cache
from collections import defaultdict, deque

@lru_cache(maxsize=None)
def can_transform_into(n1, n2):
    _n1s = sorted("".join(digits[int(i)] for i in str(n1)))
    _n2s = sorted("".join(digits[int(i)] for i in str(n2)))
    n1s = _n1s.copy()
    n2s = _n2s.copy()
    count = 0
    i = 0
    while i < len(n1s):
        if n1s[i] not in n2s:
            i += 1
        else:
            
            del n2s[n2s.index(n1s[i])]
            del n1s[i]
    # print(n1s, n2s)
    if len(n1s) + len(n2s) > 5: return False
    else: return True

# b is 15

def can_go_to(n):
    out = []
    for i in range(1, 1000):
        if can_transform_into(n, i): out.append(i)
    return out

def bi_bfs(a, b):
    a_dist = defaultdict(lambda: 99999)
    a_dist[a] = 0
    a_queue = deque()
    a_queue.append((0, a))
    b_dist = defaultdict(lambda: 99999)
    b_dist[b] = 0
    b_queue = deque()
    b_queue.append((0, b))
    both = [[a_dist, a_queue], [b_dist, b_queue]]
    switch = 0
    while True:
        distances, queue = both[switch]
        dist, n = queue.popleft()
        # print(dist, n)
        for i in can_go_to(n):
            # print(dist + 1, i)
            if i in both[1 - switch][0].keys() and both[1 - switch][0][i] != 99999: # woo win
                return dist + 1 + both[1 - switch][0][i]
            if distances[i] > dist + 1:
                distances[i] = dist + 1
                queue.append((dist + 1, i))
        switch = 1 - switch
    
def main():
    s1, f1 = [int(i) for i in input().strip().split()]
    s2, f2 = [int(i) for i in input().strip().split()]
    s3, f3 = [int(i) for i in input().strip().split()]
    print(bi_bfs(s1, f1))
    print(bi_bfs(s2, f2))
    print(bi_bfs(s3, f3))

main()

"""

b: 15

d: Yes. For any integer of any number of digits, the limit on five maximum letter-changes
allows (eventually) every digit to turn into each other. 0 can turn into 1, 2, 3, 4,; 1 can turn into 9,
5, or 7; 9 can turn into 8 and 5 into a six, so all single digits can turn into each other.
therefore all numbers of the same length can, since the digits can be changed one-by-one.
"""