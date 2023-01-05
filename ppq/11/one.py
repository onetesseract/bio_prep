alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

a, b, n = input().strip().split(" ")
a = ord(a) - ord("A") + 1
b = ord(b) - ord("A") + 1
n = int(n)
# print(a, b)

if n <= 1: n = 2

for i in range(n - 2):
    q = a + b
    a = b
    b = q%26
    # print(a, b)

print(alpha[b % 26 - 1])