class solution:
    def stairBF(self, n):
        if n == 0:
            return 1
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        return self.stairBF(n - 1) + self.stairBF(n - 2) + self.stairBF(n - 3)

    def stairTopDown(self, n):
        dp = [-1 for _ in range(n + 1)]
        return self.stairTD(dp, n)

    def stairTD(self, dp, n):
        if n == 0:
            return 1
        if n == 1:
            return 1
        if n == 2:
            return 2
        if dp[n] == -1:
            dp[n] = self.stairTD(dp, n - 1) + self.stairTD(dp, n - 2) + self.stairTD(dp, n - 3)

        return dp[n]

    def stairBU(self, n):
        dp = [-1 for _ in range(n + 1)]

        for i in range(n + 1):
            if i < 2:
                dp[i] = 1
            elif i == 2:
                dp[i] = 2
            else:
                dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
        return dp[n]

    def stairOptimized(self, n):
        i1, i2, i3, iN = 1, 1, 2, 0

        for i in range(3, n + 1):
            iN = i1 + i2 + i3
            i1 = i2
            i2 = i3
            i3 = iN
        return iN

def main():
    s = solution()
    print("Brute Force")
    print(s.stairBF(3), s.stairBF(4), s.stairBF(5))
    print("\nTop Down")
    print(s.stairTopDown(3), s.stairTopDown(4), s.stairTopDown(5))
    print("\nBottom Up")
    print(s.stairBU(3), s.stairBU(4), s.stairBU(5))
    print("\nOptimized")
    print(s.stairOptimized(3), s.stairOptimized(4), s.stairOptimized(5))

if __name__ == "__main__":
    main()
    
