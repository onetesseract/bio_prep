from math import inf

def solve(i, k, cache):
    if i == k: return (0, [])
    if i > k: return inf, []
    double = inf
    dpath = []
    if i*2 <= k and i != 0:
        if not i*2 in cache:
            cache[i*2] = solve(i*2, k, cache)
        double, dpath = cache[i*2]
    
    if not i+1 in cache:
        cache[i+1] = solve(i+1, k, cache)
    add, apath = cache[i+1]

    if double <= add:
        return (double + 1, [f"double to get {i*2}"] + dpath)
    else:
        return (add + 1, [f"add to get {i+1}"] + apath)

print(solve(0, int(input()), {}))
