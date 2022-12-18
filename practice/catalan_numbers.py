# formula is (2n)! / (n+1)!n!

def catalan_number(n):
    if n == 0 or n == 1:
        return 1
    prev = catalan_number(n - 1)
    # multiply numerator
    prev = prev * (2*n) * (2*n - 1)
    # multiply denominator
    prev = prev / ((n+1) * n)

    return prev

print(catalan_number(int(input())))
