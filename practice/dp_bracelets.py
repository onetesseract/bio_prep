def solve(index, min_price, threshold_prices, cache):
    val = -1
    price = 0
    for i in threshold_prices[index:]:
        if i > min_price:
            if not (index + 1, i) in cache:
                cache[(index + 1, i)] = solve(index + 1, i, threshold_prices, cache)
            if cache[(index + 1, i)] + (i if i < threshold_prices[index] else 0) > val:
                val = cache[(index + 1, i)] + (i if i <= threshold_prices[index] else 0)
                price = i

    return price
def main():
    cache = {}
    values = [1, 7, 2]
    min_price = 0
    for i in range(len(values)):
        min_price = solve(i, min_price, values, cache)
        print(min_price)

if __name__ == "__main__":
    main()
