# Thanks to constraints of n under 10^5 + 1, each possible number can have less than 1 comma
# So we just need the ammount of numbers from [1,000 to n], all of them have only 1 comma

class Solution:
    def countCommas(self, n: int) -> int:
        total_number = 0
        if n >= 1000:
            ammount = n - 1000 + 1
            total_number = ammount

        return total_number