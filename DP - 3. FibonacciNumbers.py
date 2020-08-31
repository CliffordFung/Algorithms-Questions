class solution:
        
    def fibBF(self, n: int):
        if n < 2:
            return n
        return self.fibBF(n - 1) + self.fibBF(n - 2)

    def fibTopDown(self, n: int):
        dp = [-1 for _ in range(n + 1)]
        ans = self.fibTD(n, dp)
        # print(dp)
        return ans

    def fibTD(self, n: int, dp):
        if n < 2:
            return n

        if dp[n] == -1:
            dp[n] = self.fibTD(n - 1, dp) + self.fibTD(n - 2, dp)
    
        return dp[n]

    def fibBU(self, n: int):
        if n < 2:
            return n

        dp = [-1] * (n + 1)

        for i in range(n + 1):
            if i < 2:
                dp[i] = i
            else:
                dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]
        
    def fibOptimized(self, n: int):
        if n < 2:
            return n
        i1 = 0
        i2 = 1
        iN = 0

        for _ in range(2, n + 1):
            iN = i1 + i2
            i1, i2 = i2, iN

        return iN

def main():
    s = solution()
    print("Brute Force:")
    print(s.fibBF(5), s.fibBF(6), s.fibBF(7))
    print("\nTop Down:")
    print(s.fibTopDown(5), s.fibTopDown(6), s.fibTopDown(7))
    print("\nBottom Up:")
    print(s.fibBU(5), s.fibBU(6), s.fibBU(7))
    print("\nMemory Optimized")
    print(s.fibOptimized(5), s.fibOptimized(6), s.fibOptimized(7))




if __name__ == "__main__":
    main()
