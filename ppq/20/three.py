# TODO: Unfinished and incorrect

from functools import lru_cache

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

@lru_cache(maxsize=None)
def sum_from(alpha_max, max_adj, max_len, _current):
    # print("called on", _current)
    if len(_current) == max_len: return 1
    current = list(_current)
    can_use_next = False
    if len(current) < max_adj: can_use_next = True
    else:
        for i in range(len(current) - 2, len(current) - 1 - max_adj, -1):
            if current[i] != current[-1]:
                can_use_next = True
                break
    
    # if not can_use_next: print("Can't use next on", current)
    total = 0
    
    current.append(-1)

    excl = current[-2] if len(current) > 1 and not can_use_next else -1

    for i in range(alpha_max):
        # print("looping for", i, excl, current)
        if i == excl:
            continue
        current[-1] = i
        total += sum_from(alpha_max, max_adj, max_len, tuple(current))
    
    return total

def solve(p, q, r, n):
    out = []
    target = n
    for i in range(r):
        out.append(-1)
        running = 0
        for i in range(p):
            out[-1] = i
            sum = sum_from(p, q, r, tuple(out))
            if running + sum >= target:
                target -= running
                break
            running += sum
    
    return "".join([alpha[i] for i in out])

def main():
    p, q, r = [int(i) for i in input().strip().split(" ")]
    n = int(input().strip())
    print(solve(p, q, r, n))

if __name__ == "__main__":
    main()