class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        minus = [inf] * (n - 1) + [nums[-1]]

        for i in range(n - 2, -1, -1):
            minus[i] = min(minus[i + 1], nums[i])

        maxus = 0
        for i in range(n):
            maxus = max(nums[i], maxus)
            if maxus - minus[i] <= k:
                return i
        return -1