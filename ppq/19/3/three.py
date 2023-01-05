from string import ascii_uppercase
from functools import lru_cache

@lru_cache(maxsize=None)
def is_valid_next(start, _letter):
    letter = ord(_letter)
    least = -1
    for _i in start[::-1]:
        i = ord(_i)
        if i < letter and i < least:
            # bad 
            return False
        if i < letter and i > least:
            # i should be new least
            least = i
    
    return True

@lru_cache(maxsize=None)
def usable_letters(start, choices):
    use = ""
    for i in choices:
        if is_valid_next(start, i) and i not in start:
            use += i
    
    return use

@lru_cache(maxsize=None)
def count_valid(letters):
    if len(letters) < 2: return len(letters)
    out = [-1]
    count = 0
    for i in letters:
        out[0] = i
        # count += sum([count_valid() for i in usable_letters(out, letters, length)]
        count += count_valid(usable_letters(str(out), ascii_uppercase))

    
    return count


@lru_cache(maxsize=None)
def blockchains_starting_with(start, length):
    usable = usable_letters(start, ascii_uppercase[:length])
    return count_valid(str(usable))

i, start = input().strip().split(" ")
i = int(i)

print(blockchains_starting_with(start, i))
