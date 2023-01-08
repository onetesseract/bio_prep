from math import factorial, comb
from functools import lru_cache
from string import ascii_uppercase

alpha = [" "] + list(ascii_uppercase) + list("0123456789")

@lru_cache(maxsize=None)
def count_len_possibilities(n, max_len): # nCr
    return comb(max_len, n)# factorial(max_len)/(factorial(max_len - n) * factorial(n))

@lru_cache(maxsize=None)
def count_len_n_starting_with_x(start, _len, max_len):
    # max_len - start # is our pool
    # print("a:", start, _len, max_len)
    return count_len_possibilities(_len, max_len - start)

def count_left(start, len_left):
    return factorial(26 + 10 - (start - 1))/factorial(26 + 10 + 1 - start - len_left)

def main(index):
    # determine len
    running_total = 0
    last = 0
    length = 0
    while running_total < index:
        length += 1
        last = running_total
        running_total += count_len_possibilities(length, 26 + 10)
    
    # print(running_total, last, length)
    offset_within = index - last
    # print(offset_within)
    last = 0
    # now we find the offset-within-th permutation of length 
    out = []
    while length != 1:
        out.append(out[-1] if len(out) != 0 else 0)
        while offset_within >= 0:
            out[-1] += 1
            last = offset_within
            offset_within -= count_len_possibilities(length - 1, 26 + 10 - out[-1])# count_len_n_starting_with_x(out[-1], length, 26 + 10)
            # print(out, offset_within)
        offset_within = last
        length -= 1
    out.append((out[-1] if len(out) != 0 else 0) + offset_within)
    
    # print(out)
    
    s = "".join(alpha[i] for i in out)
    return s

print(main(int(input().strip())))
        

    
