def main():
    print(coinChange([1, 2, 3], 5))
    print(coinChangeBottomUp([1, 2, 3], 5))

def coinChange(coins, amount):
    dp = [[-1 for i in range(amount + 1)] for c in coins]
    return coinChangeTopDown(dp, coins, amount, 0)

def coinChangeTopDown(dp, coins, total, i):
    n = len(coins)
    if total == 0:
        return 1
    
    if n == 0 or i >= n:
        return 0

    if dp[i][total] == -1:
        ways1, ways2 = 0, 0
        if coins[i] <= total:
            ways1 = coinChangeTopDown(dp, coins, total - coins[i], i)
        ways2 = coinChangeTopDown(dp, coins, total, i + 1)
        dp[i][total] = ways1 + ways2
        
    return dp[i][total]
    
def coinChangeBottomUp(coins, total):
    n = len(coins)
    if n == 0:
        return 0

    dp = [1] + [0] * total

    for i in range(n):
        for t in range(total + 1):
            print(t, coins[i])
            if coins[i] <= t:
                dp[t] += dp[t - coins[i]]
    print(dp)
    return dp[-1]
if __name__ == "__main__":
    main()

    

