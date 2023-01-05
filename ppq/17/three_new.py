from functools import lru_cache

@lru_cache(maxsize=None)
def count_parcel_permutations(weight, n, item_count):
    if weight == 0 and item_count == 0: return 1
    if weight <= 0 or item_count <= 0: return 0
    # if item_count * n < weight: return 0
    # if item_count * n == weight: return 1
    # if item_count == 1:
    #     if n >= weight: return 1
    #     else: return 0
    # if weight == 1: return 1
    count = 0
    for i in range(1, n+1):
        # if i > weight: continue
        # if i == weight: count += 1
        count += count_parcel_permutations(weight - i, i, item_count - 1)
    
    return count

@lru_cache(maxsize=None)
def count_item_permutations(parcel_count, max_item_weight, total_item_count, weight_of_parcel):
    # if parcel_count == 1: return count_parcel_permutations(weight_of_parcel, max_item_weight, total_item_count)
    if parcel_count == 0 and total_item_count == 0: return 1
    if parcel_count <= 0 or total_item_count <= 0: return 0
    # if total_item_count == 1: return 1

    count = 0
    for i in range(1, total_item_count + 1):
        count += count_parcel_permutations(weight_of_parcel, max_item_weight, i) * count_item_permutations(parcel_count - 1, max_item_weight, total_item_count - i, weight_of_parcel)
    
    return count

p, i, n, w = [int(i) for i in input().strip().split(" ")]
print(count_item_permutations(p, i, n, w))