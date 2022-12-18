import math
import sys
sys.setrecursionlimit(1 << 30)

import time
now = time.time()

def solve(index, denominations, amount_remaining, cache):
    # base case
    if amount_remaining == denominations[index]:
        return (1, [denominations[index]])
    # we can either go down a denom, or take another one out
    go_down_a_denom = math.inf
    t_path = []
    g_path = []
    if index + 1 < len(denominations):
        if not (index + 1, amount_remaining) in cache:
            cache[(index + 1, amount_remaining)] = solve(index + 1, denominations, amount_remaining, cache)
        go_down_a_denom, g_path = cache[(index + 1, amount_remaining)]

    take_another = math.inf
    if amount_remaining >= denominations[index]:
        if not (index, amount_remaining - denominations[index]) in cache:
            cache[(index, amount_remaining - denominations[index])] = solve(index, denominations, amount_remaining - denominations[index], cache)
        take_another, t_path = cache[(index, amount_remaining - denominations[index])]
        take_another += 1

    if take_another <= go_down_a_denom:
        return (take_another, [denominations[index]] + t_path)
    else:
        return (go_down_a_denom, g_path)

print(solve(0, [200, 100, 50, 20, 10, 5, 2, 1], 17450, {}))

print(time.time() - now)
    
