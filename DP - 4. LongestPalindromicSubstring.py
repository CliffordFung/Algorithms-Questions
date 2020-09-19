class longestPalStr:
    def bruteForce(self, s):
        return
    
    def topDown(self, s):
        return

    def bottomUp(self, s):
        return


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


