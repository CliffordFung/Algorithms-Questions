class HouseTheives: 
    def bruteForce(self, goods):
        return self.bruteForceRecursive(goods, 0)

    def bruteForceRecursive(self, goods, i):
        n = len(goods)
        if i >= n:
            return 0
        
        house1 = goods[i] + self.bruteForceRecursive(goods, i + 2)
        house2 = self.bruteForceRecursive(goods, i + 1)

        return max(house1, house2)

    def topDown(self, goods):
        dp = [-1 for g in goods]
        return self.topDownRecursive(dp, goods, 0)

    def topDownRecursive(self, dp, goods, i):
        n = len(goods)
        if i >= n:
            return 0
            
        if dp[i] == -1:
            house1 = goods[i] + self.topDownRecursive(dp, goods, i + 2)
            house2 = self.topDownRecursive(dp, goods, i + 1)
            dp[i] = max(house1, house2)

        return dp[i]

    def bottomUp(self, goods):
        n = len(goods)
        if n == 0:
            return 0

        dp = [0 for i in range(n + 1)]

        for i in range(1, n + 1):
            if i < 2:
                dp[i] = goods[i-1]
            else:
                house1 = goods[i-1] + dp[i - 2]
                house2 = dp[i - 1]
                dp[i] = max(house1, house2)
        return dp[n]

def main():
    s = HouseTheives()
    print("Brute Force")
    print(s.bruteForce([2, 5, 1, 3, 6, 2, 4]), s.bruteForce([2, 10, 14, 8, 1]))
    print("\nTop Down")
    print(s.topDown([2, 5, 1, 2, 6, 2, 4]), s.topDown([2, 10, 14, 8, 1]))
    print("\nBottom Up")
    print(s.bottomUp([2, 5, 1, 3, 6, 2, 4]), s.bottomUp([2, 10, 14, 8, 1]))

if __name__ == "__main__":
    main()

