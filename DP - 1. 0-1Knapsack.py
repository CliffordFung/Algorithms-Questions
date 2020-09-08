class solution:
    def knapsackBF(self, profits, weights, capacity):
        return self.knapsackRecursive(profits, weights, capacity, 0)
    
    def knapsackRecursive(self, profits, weights, capacity, i): 
        n = len(profits)
        if n != len(weights) or n == 0 or capacity == 0 or i >= n: 
            return 0
        
        profit1 = 0
        profit2 = self.knapsackRecursive(profits, weights, capacity, i + 1)

        if weights[i] <= capacity:
            profit1 = profits[i] + self.knapsackRecursive(profits, weights, capacity - weights[i], i + 1)
        
        return max(profit1, profit2)
    
    def knapsackTopDown(self, profits, weights, capacity):
        return
    
    
    
def main():
    s = solution()
    print("Brute Force")
    print(s.knapsackBF([1, 6, 10, 16], [1, 2, 3, 5], 7), s.knapsackBF([1, 6, 10, 16], [1, 2, 3, 5], 6))
    # print("\nTop Down")
    # print(s.stairTopDown(3), s.stairTopDown(4), s.stairTopDown(5))
    # print("\nBottom Up")
    # print(s.stairBU(3), s.stairBU(4), s.stairBU(5))
    # print("\nOptimized")
    # print(s.stairOptimized(3), s.stairOptimized(4), s.stairOptimized(5))


if __name__ == "__main__":
    main()
