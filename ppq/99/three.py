denoms = []
from functools import lru_cache
from math import inf

@lru_cache(maxsize=None)
def minimise_denominations(denoms_offset, amount, history):
    # print(denoms_offset, amount)
    global denoms
    # first base cases
    if amount == 0: return (0, history)

    if amount < min(denoms): # is impossibel
        return (inf, ())
    # we have a choice
    # either go down a denom, or dont
    

    take_another_out = (inf, ())
    # can we take another out
    if denoms[denoms_offset] <= amount: # yes we can
        val, hist = minimise_denominations(denoms_offset, amount - denoms[denoms_offset], history + (denoms[denoms_offset],))
        val += 1
        take_another_out = (val, hist)
    
    go_down_a_denom = (inf, ())
    
    # can we go down a denom
    if denoms_offset + 1 != len(denoms):
        # yes, we can
        go_down_a_denom = minimise_denominations(denoms_offset + 1, amount, history)
    
    # print(take_another_out, go_down_a_denom, min(take_another_out, go_down_a_denom))
    return min(take_another_out, go_down_a_denom)

def collect(history):
    i = 0
    out = []
    while i != len(history):
        q = 0
        while i + q != len(history) and history[i + q] == history[i]: q += 1
        out.append((history[i], q))
        i += q
    return " ".join([f"{n}x{v}" for (v, n) in out])

_ = input()
denoms = list(reversed(sorted([int(i) for i in input().strip().split()])))
_ = input()
scores = [int(i) for i in input().strip().split()]

# print(denoms)

for i in scores:
    count, hist = minimise_denominations(0, i, ())
    if count == inf: print("Impossible")
    else:
        print(count, collect(hist))


# b: 2 rounds, 81/1
#  : 4: 81/27+3+1