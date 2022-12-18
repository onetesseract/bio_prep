import math

num = 600851475143
for i in range(1, math.ceil(math.sqrt(num*2)), 2):
    if num%i == 0:
        if num == i:
            break
        num /= i

print(num)
