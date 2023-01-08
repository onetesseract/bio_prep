from functools import lru_cache
from math import factorial

@lru_cache(maxsize=None)
def count_arrangements(a, b, c, d):
    # first, without compensation
    options = a + b + c + d #sum([1 for i in [a, b, c, d] if i != 0])
    total = factorial(options)
    # print(options, total)
    # now we compensate for the duplicates we've created
    # is this the way?
    for i in [a, b, c, d]:
        total /= factorial(i)
    # if a != 0:
    #     total /= a
    # if b != 0:
    #     total /= b
    # if c != 0:
    #     total /= c
    # if d != 0:
    #     total /= d
    
    return total

def find_n(a, b, c, d, n):
    # take the a
    arr = []
    while n > 0:
        print(a, b, c, d, arr, n)
        a_start = count_arrangements(a - 1, b, c, d) if a > 0 else 0
        print(a_start)
        if a_start >= n:
            # a is def start
            arr.append("A")
            a -= 1
            # no change in n
            break
        b_start = count_arrangements(a, b - 1, c, d) if b > 0 else 0
        print(b_start)
        if a_start + b_start >= n:
            arr.append("B")
            b -= 1
            n -= a_start
            break
        c_start = count_arrangements(a, b, c - 1, d) if c > 0 else 0
        print(c_start)
        if a_start + b_start + c_start >= n:
            arr.append("C")
            c -= 1
            n -= a_start + b_start
            break
        d_start = count_arrangements(a, b, c, d - 1) if d > 0 else 0
        print(d_start)
        if a_start + b_start + c_start + d_start >= n:
            arr.append("D")
            d -= 1
            n -= a_start + b_start + c_start
            break
    
    return arr

def find_n_good(a, b, c, d, n):
    if a + b + c + d == 0: return []
    arr = []
    new_n = n
    if a > 0:
        new_n -= count_arrangements(a - 1, b, c, d)
        if new_n < 0:
            # a is hit
            arr = ["A"]
            return arr + find_n_good(a - 1, b, c, d, n)
    if b > 0:
        # print("After a, n", new_n)
        n = new_n
        new_n -= count_arrangements(a, b - 1, c, d)
        if new_n < 0:
            arr = ["B"]
            return arr + find_n_good(a, b - 1, c, d, n)
    if c > 0:
        # print("After b, n", new_n)
        n = new_n
        new_n -= count_arrangements(a, b, c - 1, d)
        if new_n < 0:
            arr = ["C"]
            return arr + find_n_good(a, b, c - 1, d, n)
    if d > 0:
        n = new_n
        new_n -= count_arrangements(a, b, c, d - 1)
        if new_n < 0:
            arr = ["D"]
            return arr + find_n_good(a, b, c, d - 1, n)
        return None


a, b, c, d, n = [int(i) for i in input().strip().split(" ")]
print("".join(find_n_good(a, b, c, d, n - 1)))
