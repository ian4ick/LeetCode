class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        if nums[0] - min(nums) <= k:
            return 0
        for i in range(1, len(nums)):
            instability = max(nums[0:i]) - min(nums[i:])
            if instability <= k:
                return i
        return -1