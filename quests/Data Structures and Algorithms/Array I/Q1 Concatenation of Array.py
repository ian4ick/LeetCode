class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        return [nums[i%len(nums)] for i in range(2 * len(nums))]