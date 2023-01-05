import math

interest, repayment = [int(i)/100 for i in input().strip().split(" ")]

def r_up_to_2dp(num):
    return math.ceil(round(num, 8)) 

paid_back = 0
count = 0

owed = 10000
while owed != 0:
    owed *= (interest + 1)
    owed = r_up_to_2dp(owed)
    payback = r_up_to_2dp(max(owed * repayment, 5000))
    if payback > owed:
        payback = owed
    paid_back += payback
    owed -= payback
    owed = r_up_to_2dp(owed)
    count += 1
    # print(payback, owed)

print(paid_back / 100, count)
