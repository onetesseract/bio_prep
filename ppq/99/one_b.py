def next_digital_river(n):
    return n + sum([int(i) for i in str(n)])



def main():
    r1 = [1]
    r3 = [3]
    r9 = [9]
    river = [int(input())]
    while True:
        if r1[-1] in river:
            return "First meets river 1 at " + str(r1[-1])
        if r3[-1] in river:
            return "First meets river 1 at " + str(r3[-1])
        if r9[-1] in river:
            return "First meets river 1 at " + str(r9[-1])
        r1.append(next_digital_river(r1[-1]))
        r3.append(next_digital_river(r3[-1]))
        r9.append(next_digital_river(r9[-1]))
        if river[-1] in r1:
            return "First meets river 1 at " + str(river[-1])
        if river[-1] in r3:
            return "First meets river 3 at " + str(river[-1])
        if river[-1] in r9:
            return "First meets river 9 at " + str(river[-1])
        river.append(next_digital_river(river[-1]))

# print(main())

from collections import defaultdict
count = defaultdict(int)

i = 1
while True:
    last = i
    count[last] += 1
    if count[last] == 100:
        print(last)
        exit(0)
    for _ in range(10000):
        last = next_digital_river(last)
        count[last] += 1
        if count[last] == 100:
            print(last)
            exit(0)
    i += 1

# 1003