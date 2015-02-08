def knapsack(capacity, items):
    result = [0] * len(items)
    ratios = sorted(enumerate(items), key=lambda k: float(k[1][1]) / k[1][0],
                    reverse=True)

    def add_item(capacity):
        for item in ratios:
            if capacity >= item[1][0]:
                result[item[0]] += 1
                return capacity - item[1][0]
    while capacity:
        capacity = add_item(capacity)
    return result


print knapsack(100, [[100, 1]])
