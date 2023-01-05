from functools import lru_cache

combinations = set()

optns = [i for i in range(1, 10)]

target = 3

@lru_cache(maxsize=None)
def all_that_adds_to(target):
    if target == 0: return [[]]
    if target == 1: return [[1]]
    else:
        out = []
        for i in range(1, min(target + 1, 9)):
            for q in all_that_adds_to(target - i):
                out.append([i] + q)
    
        return out

def main():
    target, n = [int(i) for i in input().strip().split(" ")]

    print(" ".join([str(i) for i in all_that_adds_to(target)[n - 1]]))

if __name__ == "__main__":
    main()