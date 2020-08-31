
from math import inf
class solution:
    ''' top-down '''
    def maxRibbonCut(self, ribbonLengths, total) -> int:
        dp = [[-1 for i in range(total + 1)] for _ in ribbonLengths]
        ans = self.maxRibbonCutTopDown(dp, ribbonLengths, total, 0)
        return - 1 if ans == -inf else ans
        
    def maxRibbonCutTopDown(self, dp, ribbonLengths, total, i):
        n = len(ribbonLengths)
        if total == 0:
            return 0
        if n == 0 or i >= n:
            return -inf

        if dp[i][total] == -1:
            cuts1 = -inf
            cuts2 = -inf

            if ribbonLengths[i] <= total:
                cuts1 = 1 + self.maxRibbonCutTopDown(dp, ribbonLengths, total - ribbonLengths[i], i)
            cuts2 = self.maxRibbonCutTopDown(dp, ribbonLengths, total, i + 1)
            
            dp[i][total] = max(cuts1, cuts2)

        return dp[i][total]
        
    def maxRibbonCutBottomUp(self, ribbonLengths, total) -> int:
        n = len(ribbonLengths)
        
        if n == 0:
            return - 1
        
        dp = [0] + [-inf] * total

        for i in range(n):
            for t in range(total + 1):
                cuts1 = -inf
                cuts2 = dp[t]
                if ribbonLengths[i] <= t:
                    cuts1 = dp[t - ribbonLengths[i]] + 1
                dp[t] = max(cuts1, cuts2)
                
        ans = dp[total]
        return -1 if ans == -inf else ans 
    
def main():
    s = solution()
    print(s.maxRibbonCut([2, 3, 5], 5))
    print(s.maxRibbonCut([2, 3], 7))
    print(s.maxRibbonCut([3, 5, 7], 13))
    print(s.maxRibbonCut([3, 5], 7))

    print(s.maxRibbonCutBottomUp([2, 3, 5], 5))
    print(s.maxRibbonCutBottomUp([2, 3], 7))
    print(s.maxRibbonCutBottomUp([3, 5, 7], 13))
    print(s.maxRibbonCutBottomUp([3, 5], 7))


if __name__ == "__main__":
    main()
