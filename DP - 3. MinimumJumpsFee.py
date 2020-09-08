class solution: 
    def jumpMinFeesBF(self, fees):
        return self.jumpMinFeesBFRecursive(fees, 0)

    def jumpMinFeesBFRecursive(self, fees, i):
        n = len(fees)
        if i >= n:
            return 0

        fee1 = self.jumpMinFeesBFRecursive(fees, i + 1) + fees[i]
        fee2 = self.jumpMinFeesBFRecursive(fees, i + 2) + fees[i]
        fee3 = self.jumpMinFeesBFRecursive(fees, i + 3) + fees[i]
        
        minimum_fee = min(fee1, fee2, fee3)

        return minimum_fee

    def jumpMinFeesTopDown(self, fees):
        dp = [-1 for i in fees]
        return self.jumpMinFeesTD(dp, fees, 0)

    def jumpMinFeesTD(self, dp, fees, i):
        n = len(fees)
        if i >= n:
            return 0
            
        if dp[i] == -1:
            fees1 = self.jumpMinFeesTD(dp, fees, i + 1) + fees[i]
            fees2 = self.jumpMinFeesTD(dp, fees, i + 2) + fees[i]
            fees3 = self.jumpMinFeesTD(dp, fees, i + 3) + fees[i]
            dp[i] = min(fees1, fees2, fees3)
        return dp[i]

    def jumpMinFeesBottomUp(self, fees):
        n = len(fees)
        if n == 0:
            return 0

        dp = [0] * (n + 1)

        for i in range(n + 1):
            if i == 0:
                dp[i] = 0
            elif i < 3:
                dp[i] = fees[0]
            else:
                dp[i] = min(fees[i - 1] + dp[i - 1], fees[i - 2] + dp[i - 2], fees[i - 3] + dp[i - 3])
        
        return dp[n]

def main():
    s = solution()

    print("Brute Force")
    print(s.jumpMinFeesBF([1, 2, 5, 2, 1, 2]), s.jumpMinFeesBF([2, 3, 4, 5]))
    print("\nTop Down")
    print(s.jumpMinFeesTopDown([1, 2, 5, 2, 1, 2]), s.jumpMinFeesTopDown([2, 3, 4, 5]))
    print("\nBottom Up")
    print(s.jumpMinFeesBottomUp([1, 2, 5, 2, 1, 2]), s.jumpMinFeesBottomUp([2, 3, 4, 5]))

if __name__ == "__main__":
    main()
