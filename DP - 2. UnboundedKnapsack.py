def main():
    weights1 = [1, 2, 3]
    profits1 = [15, 20, 50]
    capacity1 = 5
    print(unboundedKnapsack(weights1, profits1, capacity1))
    print(unboundedKnapsack([1, 3, 4, 5], [15, 50, 60, 90], 8))
    print(unboundedKnapsack([1, 3, 4, 5], [15, 50, 60, 90], 6))

    print(unboundedKnapsackBottomUp(weights1, profits1, capacity1))
    print(unboundedKnapsackBottomUp([1, 3, 4, 5], [15, 50, 60, 90], 8))
    print(unboundedKnapsackBottomUp([1, 3, 4, 5], [15, 50, 60, 90], 6))
    print(unboundedKnapsackBottomUp([1, 2, 3, 5], [1, 6, 10, 16], 5))

def unboundedKnapsack(weights, profits, capacity):
    dp = [[-1 for c in range(capacity + 1)] for item in profits]
    return unboundedKnapsackTopDown(dp, weights, profits, capacity, 0)

def unboundedKnapsackBottomUp(weights, profits, capacity):
    n = len(weights)
    if capacity <= 0 or n == 0 or n != len(profits):
        return 0

    dp = [[0 for _ in range(capacity + 1)] for _ in weights]

    for i in range(n):
        for c in range(capacity + 1):
            profit1 = 0
            profit2 = 0
            if i > 0:
                profit1 = dp[i - 1][c]
            if weights[i] <= c:
                profit2 = profits[i] + dp[i][c - weights[i]]
            dp[i][c] = max(profit1, profit2)
    return dp[n - 1][capacity]


def unboundedKnapsackTopDown(dp, weights, profits, capacity, i):
    n = len(weights)
    if i >= n or n != len(profits) or n == 0 or capacity <= 0:
        return 0

    if dp[i][capacity] == -1:
        profit1 = 0
        if weights[i] <= capacity:
            profit1 = profits[i] + unboundedKnapsackTopDown(
                dp, weights, profits, capacity - weights[i], i)

        profit2 = unboundedKnapsackTopDown(
            dp, weights, profits, capacity, i + 1)

        dp[i][capacity] = max(profit1, profit2)

    return dp[i][capacity]



if __name__ == "__main__":
    main()

