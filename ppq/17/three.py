from math import floor
from functools import lru_cache

import sys
sys.setrecursionlimit(1 << 10)

@lru_cache(maxsize=None)
def permute_items(max_parcel_weight, item_weights):
    if len(item_weights) == 1 :
        if max_parcel_weight % item_weights[0] != 0: return []
        else: return [item_weights[0]] * int(max_parcel_weight/item_weights[0])
    if max_parcel_weight <= 0: return []
    out = []
    for i in range(len(item_weights)):
        for j in range(1, floor(max_parcel_weight/item_weights[i])):
            out += [ ([item_weights[i]] * j + permute_items(max_parcel_weight - item_weights[i]*j, item_weights[:i] + item_weights[i+1:]))]
    
    return out
        


def main():
    parcel_count, max_item_weight, item_count, parcel_weight

if __name__ == "__main__":
    main()