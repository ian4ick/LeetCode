from itertools import permutations

class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        cnt = 0
        uniques = set()

        for p in permutations(digits, 3):
            num = p[0] * 100 + p[1] * 10 + p[2]
            if p[0] != 0 and p[2] % 2 == 0:
                uniques.add(num)

        return len(uniques)