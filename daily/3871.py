class Solution:
    def countCommas(self, n: int) -> int:
        if n < 10**3:
            return 0
        total = (n - 10 ** 3 + 1)
        if n >= 10 ** 6:
            total += (n - 10 ** 6 + 1)
        if n >= 10 ** 9:
            total += (n - 10 ** 9 + 1)
        if n >= 10 ** 12:
            total += (n - 10 ** 12 + 1)
        total += int(n == 10 ** 15)
        return total