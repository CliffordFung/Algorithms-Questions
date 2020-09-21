class longestPalStr:
    def bruteForce(self, s):
        return self.bruteForceR(s, 0, len(s) - 1)

    def bruteForceR(self, s, start, end):
        n = len(s)
        if start > end:
            return 0

        if start == end:
            return 1

        if s[start] == s[end]:
            remaining_len = end - start - 1
            if remaining_len == self.bruteForceR(s, start + 1, end - 1): 
                return 2 + self.bruteForceR(s, start + 1, end - 1)
        
        len1 = self.bruteForceR(s, start + 1, end)
        len2 = self.bruteForceR(s, start, end - 1)

        return max(len1, len2)
        
    
    def topDown(self, s):
        n = len(s)
        dp = [[-1 for s in range(n)] for e in range(n)]
        return self.topDownR(dp, s, 0, n - 1)

    def topDownR(self, dp, s, start, end):
        n = len(s)

        if start > end:
            return 0

        if start == end:
            return 1

        if dp[start][end] == -1:
            if s[start] == s[end]:
                remaining_len = end - start - 1
                if remaining_len == self.topDownR(dp, s, start + 1, end - 1):
                    dp[start][end] = 2 + remaining_len
                    return dp[start][end]

            len1 = self.topDownR(dp, s, start + 1, end)
            len2 = self.topDownR(dp, s, start, end - 1)
            dp[start][end] = max(len1, len2)

        return dp[start][end]

    def bottomUp(self, s):
        n = len(s)
        if n == 0:
            return 0

        dp = [[False for start in range(n)] for end in range(n)]

        for i in range(n):
            dp[i][i] = True

        max_length = 1
        for start in range(n - 1, -1, -1):
            for end in range(start + 1, n):
                if s[start] == s[end]:
                    remaining_len = end - start - 1
                    if remaining_len == 1 or dp[start + 1][end - 1]:
                        dp[start][end] = True
                        max_length = max(max_length, 2 + remaining_len)
        
        return max_length

def main():
    solution = longestPalStr()

    print("Brute Force")
    print(solution.bruteForce("abdbca"), solution.bruteForce("cddpd"), solution.bruteForce("pqr"))
    print("\nTop Down")
    print(solution.topDown("abdbca"), solution.topDown("cddpd"), solution.topDown("pqr"))
    print("\nBottom Up")
    print(solution.bottomUp("abdbca"), solution.bottomUp("cddpd"), solution.bottomUp("pqr"))


if __name__ == "__main__":
    main()


