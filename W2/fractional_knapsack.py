arr = [(5, 10), (3, 20), (8, 25), (4, 8)]
W = 13


def fractional_knapsack(arr, W):
    density = []
    knapsack = []
    total_value = 0

    for index, item in enumerate(arr):
        cost = item[1]/item[0]
        density.append((index, cost))

    density.sort(key=lambda x: x[1], reverse=True)

    for elm in density:
        if W - arr[elm[0]][0] >= 0:
            knapsack.append((elm[0], 1))
            W -= arr[elm[0]][0]
            total_value += arr[elm[0]][1]
        else:
            fraction = W/arr[elm[0]][0]
            knapsack.append((elm[0], fraction))
            W -= (arr[elm[0]][0] * fraction)
            total_value += (arr[elm[0]][1] * fraction)
            break

    return total_value, knapsack


print(fractional_knapsack(arr, W))
