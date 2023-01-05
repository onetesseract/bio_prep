from functools import lru_cache
from math import floor

@lru_cache(maxsize=None)
def count_splits(word):
    # print("Valid:", pred, word, pred)
    # print("Trying", word)
    if len(word) == 1: return 1
    if len(word) == 0: return 1
    count = 1
    for i in range(1, floor(len(word) / 2) + 1):
        # print("Trying", word[:i], word[len(word) - i:])
        if word[:i] == word[len(word) - i:]:
            # is valid
            count += count_splits(word[i:len(word) - i]) if len(word) != 2 * i else 1
    
    return count

print(count_splits(input().strip()) - 1)

"""
A ABCBA A
A A BCB A A
A A B C B A A
AA BCB AA
AA B C B AA
"""