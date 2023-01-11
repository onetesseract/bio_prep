import math

"""
def factorize(n):
    # print(n)
    n = round(n)
    out = []
    if n % 2 == 0:
            # i is a prime factor
            # take it out all the time
            while n % 2 == 0:
                # print("hit 2")
                n /= 2
            # n *= 2
            # n = round(n)
            out.append(2)
            out += factorize(n)
            return out
    for i in range(3, math.ceil(n ** 0.5) + 1, 2):
        if n % i == 0:
            # i is a prime factor
            while n % i == 0:
                # print("hit", i)
                n /= i
            # n *= i
            # n = round(n)
            out.append(i)
            out += factorize(n)
            return out
    if out == []: return [n]

n = int(input())
count = 1
done = []
f = factorize(n)
# print(f)
for i in f:
    count *= i

print(count)
"""

out = []

for fives in range(1, 50):
    for twos in range(1, 100):
        q = (2**twos) * (5**fives)
        out.append(q)
print(len(out))

out = sorted(out)
print(out[:15])

"""
b:
10 = 2... * 5...

"""

# 10, 20, 40, 50, 80, 100, 160, 200, 250, 320