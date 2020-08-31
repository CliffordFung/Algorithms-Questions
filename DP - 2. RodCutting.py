def main():
    print(rodCuttingTopDown([1, 2, 3, 4, 5], [2, 6, 7, 10, 13], 5))
    print(rodCuttingBottomUp([1, 2, 3, 4, 5], [2, 6, 7, 10, 13], 5))

def rodCuttingTopDown(lengths, prices, n):
    dp = [[-1 for _ in range(len(lengths) + 1)] for item in prices]
    return rodCuttingTopDownRecursive(dp, lengths, prices, n, 0)
    
def rodCuttingTopDownRecursive(dp, lengths, prices, n, i):
    if len(prices) != len(lengths) or n == 0 or i >= n:
        return 0

    if dp[i][n] == -1:
        profit1 = 0
        profit2 = 0

        if lengths[i] <= n:
            profit1 = prices[i] + rodCuttingTopDownRecursive(dp, lengths, prices, n - i - 1, i)
        profit2 = rodCuttingTopDownRecursive(dp, lengths, prices, n, i + 1)
        dp[i][n] = max(profit1, profit2)

    return dp[i][n]
    
def rodCuttingBottomUp(lengths, prices, n):
    if len(prices) != len(lengths) or n == 0:
        return 0

    dp = [[0 for _ in range(n + 1)] for _ in prices]

    for i in range(n):
        for l in range(n + 1):
            profit1, profit2 = 0, 0
            if lengths[i] <= l:
                profit1 = prices[i] + dp[i][l - lengths[i]]
            if i > 0:
                profit2 = dp[i - 1][l]
            dp[i][l] = max(profit1, profit2)

    return dp[n-1][n]
        

if __name__ == "__main__":
    main()
