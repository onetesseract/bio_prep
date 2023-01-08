total_mod = 24 * 60

a, b = [int(i) for i in input().strip().split()]

a_time = 0
b_time = 0

a_time += 60 + a
b_time += 60 + b
a_time = a_time % total_mod
b_time = b_time % total_mod

while a_time != b_time:
    a_time += 60 + a
    b_time += 60 + b
    a_time = a_time % total_mod
    b_time = b_time % total_mod

from math import floor

hours = str(floor(a_time / 60))
hours = hours if len(hours) == 2 else "0" + hours
mins = str(a_time % 60)
mins = mins if len(mins) == 2 else "0" + mins

print(hours + ":" + mins)