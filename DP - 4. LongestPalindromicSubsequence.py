class PalindromicSub: 
    def bruteForce(self, s):
        return self.bruteForceR(s, 0, len(s) - 1)

    def bruteForceR(self, s, start, end):
        n = len(s)
        if start > end:
            return 0
        if start == end:
            return 1
        
        if s[start] == s[end]:
            return 2 + self.bruteForceR(s, start + 1, end - 1)
        
        len1 = self.bruteForceR(s, start + 1, end)
        len2 = self.bruteForceR(s, start, end - 1)

        return max(len1, len2)

        
    def topDown(self, s):
        n = len(s)
        # dp = {}
        # return self.topDownR(dp, s, 0, len(s) - 1)
        dp = [[-1 for _ in range(n)] for _ in range(n)]
        return self.topDown2D(dp, s, 0, n - 1)
        
    def topDown2D(self, dp, s, start, end):
        n = len(s)

        if start > end:
            return 0

        if start == end:
            return 1

        if dp[start][end] == -1:
            if s[start] == s[end]:
                dp[start][end] = 2 + self.topDown2D(dp, s, start + 1, end - 1)
            else:
                len1 = self.topDown2D(dp, s, start + 1, end)
                len2 = self.topDown2D(dp, s, start, end - 1)
                dp[start][end] = max(len1, len2)

        return dp[start][end]


    
    # hashmap solution
    def topDownR(self, dp, s, start, end):
        if start > end:
            return 0
        
        if start == end:
            return 1
            
        if str(start) + "|" + str(end) not in dp:
            if s[start] == s[end]:
                dp[str(start) + "|" + str(end)] = 2 + self.topDownR(dp, s, start + 1, end - 1)
            else: 
                len1 = self.topDownR(dp, s, start + 1, end)
                len2 = self.topDownR(dp, s, start, end - 1)
                dp[str(start) + "|" + str(end)] = max(len1, len2)
        return dp[str(start) + "|" + str(end)]

    def bottomUp(self, s):
        n = len(s)

        if n < 2:
            return n

        dp = [[0 for _ in range(n)] for _ in range(n)]

        for i in range(n): 
            dp[i][i] = 1

        for start in range(n - 1, -1, -1):
            for end in range(start + 1, n):
                if s[start] == s[end]:
                    dp[start][end] = 2 + dp[start + 1][end - 1]
                else:
                    len1 = dp[start + 1][end]
                    len2 = dp[start][end - 1]
                    dp[start][end] = max(len1, len2)
        return dp[0][n-1]

def main():
    sol = PalindromicSub()
    print("Brute Force")
    print(sol.bruteForce("abdbca"), sol.bruteForce("cddpd"), sol.bruteForce("pqr"))
    print("\nTop Down")
    print(sol.topDown("abdbca"), sol.topDown("cddpd"), sol.topDown("pqr"))
    print("\nBottom Up")
    print(sol.bottomUp("abdbca"), sol.bottomUp("cddpd"), sol.bottomUp("pqr"))

if __name__ == "__main__":
    main()

