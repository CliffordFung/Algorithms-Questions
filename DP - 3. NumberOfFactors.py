class solution:
    def numFactorsBF(self, n):
        if n < 3:
            return 1
        if n == 3:
            return 2
        if n == 4:
            return 4
        
        return self.numFactorsBF(n - 1) + self.numFactorsBF(n - 3) + self.numFactorsBF(n - 4)

    def numFactorsTopDown(self, n):
        dp = [-1 for _ in range(n + 1)]
        return self.numFactorsTD(dp, n)

    def numFactorsTD(self, dp, n):
        if n < 3:
            dp[n] = 1

        if n == 3:
            dp[n] = 2
        
        if dp[n] == -1:
            dp[n] = self.numFactorsTD(dp, n - 1) + self.numFactorsTD(dp, n - 3) + self.numFactorsTD(dp, n - 4)

        return dp[n]

    def numFactorsBU(self, n):
        dp = [-1 for _ in range(n + 1)]

        for i in range(n + 1):
            if i < 3:
                dp[i] = 1
            elif i == 3:
                dp[i] = 2
            else:
                dp[i] = dp[i - 1] + dp[i - 3] + dp[i - 4]

        return dp[n]

    def numFactorsOptimized(self, n):
        if n < 3:
            return 1
        if n == 3:
            return 2

        i1, i2, i3, i4 = 1, 1, 1, 2
        iN = 0

        for _ in range(4, n + 1):
            iN = i1 + i2 + i4
            i1, i2, i3, i4 = i2, i3, i4, iN
        return iN

def main():
    s = solution()
    print("Brute Force")
    print(s.numFactorsBF(4), s.numFactorsBF(5), s.numFactorsBF(6))
    print("\nTop Down")
    print(s.numFactorsTopDown(4), s.numFactorsTopDown(5), s.numFactorsTopDown(6))
    print("\nBottom Up")
    print(s.numFactorsBU(4), s.numFactorsBU(5), s.numFactorsBU(6))
    print("\nOptimized")
    print(s.numFactorsOptimized(4), s.numFactorsOptimized(5), s.numFactorsOptimized(6))

if __name__ == "__main__":
    main()
        
