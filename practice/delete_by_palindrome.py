import math
from functools import lru_cache

@lru_cache()
def is_palindrome(string):
    return string[:math.floor(len(string)/2)] == string[math.ceil(len(string)/2):][::-1]

@lru_cache()
def find_palindromes(string):
    index_pairs = []
    for i in range(len(string)):
        for j in range(1, len(string) - i):
            if string[j + i] == string[i]:
                print(f"{string[j + i]} is dup, trying {string[i:i+j+1]}")
                if is_palindrome(string[i:i + j + 1]):
                    index_pairs.append((i, i + j + 1))

    return index_pairs

def solve(string):
    if len(string) == 0: return (0, [])
    if len(string) == 1: return (1, [])
    choices = find_palindromes(string)
    min = math.inf
    delete = (0, 0)
    path = []
    for (index, index2) in choices:
        s = string[:index] + string[index2 + 1:]
        val, possible_path = solve(s)
        if val < min:
            min = val
            delete = (index, index2)
            path = possible_path
    
    d1, d2 = delete
    print(d1, d2)
    return (min, [string[d1:d2 + 1]] + path)

print(solve(input("")))
