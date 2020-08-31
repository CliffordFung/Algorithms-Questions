from math import inf

def main():
    print(minCoinChange([1, 2, 3], 5))
    print(minCoinChange([1, 2, 3], 11))
    print(minCoinChange([1, 2, 3], 7))
    print(minCoinChange([3, 5], 7))
    print(minCoinChangeBottomUp([1, 2, 3], 5))
    print(minCoinChangeBottomUp([1, 2, 3], 11))
    print(minCoinChangeBottomUp([1, 2, 3], 7))
    print(minCoinChangeBottomUp([3, 5], 7))

def minCoinChange(coins, total):
    dp = [[-1 for _ in range(total + 1)] for _ in coins]
    ans = minCoinChangeTopDown(dp, coins, total, 0)
    return -1 if ans == inf else ans
    
def minCoinChangeTopDown(dp, coins, total, i):
    if total == 0:
        return 0
        
    n = len(coins)
    if n == 0 or i >= n:
        return inf

    if dp[i][total] == -1:
        count1 = inf
        if coins[i] <= total:
            count1 = minCoinChangeTopDown(dp, coins, total - coins[i], i)
        if count1 != inf:
            count1 += 1
        count2 = minCoinChangeTopDown(dp, coins, total, i + 1)
        dp[i][total] = min(count1, count2)

    return dp[i][total]


def minCoinChangeBottomUp(coins, amount):
    if amount == 0:
        return 0

    n = len(coins)

    dp = [0] + [inf] * amount

    for i in range(n):
        for a in range(amount + 1):
            count1 = inf
            count2 = dp[a]
            if coins[i] <= a:
                count1 = dp[a - coins[i]]
                if count1 != inf:
                    count1 += 1
            dp[a] = min(count1, count2)

    return -1 if dp[-1] == inf else dp[-1]


if __name__ == '__main__':
    main()
