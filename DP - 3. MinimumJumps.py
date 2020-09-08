import math

class solution: 
    def minJumpsBF(self, jumps):
        return self.minJumpsBFRecursive(jumps, 0)

    def minJumpsBFRecursive(self, jumps, i):
        n = len(jumps)

        if i == n - 1:
            return 0
        
        if jumps[i] == 0:
            return math.inf

        totalJumps = math.inf
        start = i + 1
        end = i + jumps[i]
        while start < n and start <= end:
            jumps1 = 1 + self.minJumpsBFRecursive(jumps, start)
            jumps2 = totalJumps
            totalJumps = min(jumps1, jumps2)
            start += 1
        
        return totalJumps

    def minJumpsTopDown(self, jumps):
        dp = [-1 for j in jumps]
        ans = self.minJumpsTD(dp, jumps, 0)        
        return -1 if ans == math.inf else ans

    def minJumpsTD(self, dp, jumps, i):
        n = len(jumps)
        if i == n - 1:
            return 0

        if jumps[i] == 0:
            return math.inf
        
        if dp[i] == -1:
            totalJumps = math.inf
            start = i + 1
            end = i + jumps[i]
            while start < n and start <= end:
                jumps1 = 1 + self.minJumpsTD(dp, jumps, start)
                dp[i] = min(totalJumps, jumps1)
                start += 1

        return dp[i]

    def minJumpsBU(self, jumps):
        n = len(jumps)
        if n == 0:
            return 0
        
        dp = [0] + [math.inf] * (n - 1)

        for start in range(n):
            end = start + 1
            while end < n and end <= start + jumps[start]:
                dp[end] = min(dp[end], dp[start] + 1)
                end += 1
        
        return dp[n - 1]

def main():
    s = solution()
    print("BruteForce")
    print(s.minJumpsBF([2, 1, 1, 1, 4]),
          s.minJumpsBF([1, 1, 3, 6, 9, 3, 0, 1, 3]))
    print("\nTop Down")
    print(s.minJumpsTopDown([2, 1, 1, 1, 4]),
          s.minJumpsTopDown([1, 1, 3, 6, 9, 3, 0, 1, 3]))
    print("\nBottom Up")
    print(s.minJumpsBU([2, 1, 1, 1, 4]),
          s.minJumpsBU([1, 1, 3, 6, 9, 3, 0, 1, 3]))

if __name__ == "__main__":
    main()

        
