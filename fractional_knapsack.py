from sys import stdin

def optimal_value(capacity, weights, values):
    # Create a list of tuples with (value-to-weight ratio, value, weight)
    appraisal = []
    for i in range(len(values)):
        ratio = values[i] / weights[i]
        appraisal.append((ratio, values[i], weights[i]))
    
    # Sort the items by the value-to-weight ratio in descending order
    appraisal.sort(reverse=True, key=lambda x: x[0])

    # Calculate the maximum value that can be carried in the knapsack
    value = 0.0
    for ratio, value_i, weight_i in appraisal:
        if capacity == 0:
            break
        # Take as much of the item as possible
        amount = min(weight_i, capacity)
        value += amount * ratio
        capacity -= amount

    return value

if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:2 + 2 * n:2]
    weights = data[3:2 + 2 * n:2]
    opt_value = optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
