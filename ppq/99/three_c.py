denoms = list(reversed([1, 4, 5, 17, 28, 43, 100]))

from functools import lru_cache
from math import inf

@lru_cache(maxsize=None)
def minimise_denominations(denoms_offset, amount):
    # print(denoms_offset, amount)
    global denoms
    # first base cases
    if amount == 0: return 1

    if amount < min(denoms): # is impossibel
        return 0
    # we have a choice
    # either go down a denom, or dont
    

    take_another_out = 0
    # can we take another out
    if denoms[denoms_offset] <= amount: # yes we can
        take_another_out = minimise_denominations(denoms_offset, amount - denoms[denoms_offset])
    
    go_down_a_denom = 0
    
    # can we go down a denom
    if denoms_offset + 1 != len(denoms):
        # yes, we can
        go_down_a_denom = minimise_denominations(denoms_offset + 1, amount)
    
    # print(take_another_out, go_down_a_denom, min(take_another_out, go_down_a_denom))
    return take_another_out + go_down_a_denom

print(minimise_denominations(0, 100))
# 1333