class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        d = dict().fromkeys([i for i in nums], 0)
        res = [0, 0]
        for i in range(1, len(nums) + 1):
            if i not in d.keys():
                res[1] = i
                break
        for i in nums:
            d[i] += 1
        for i in d.keys():
            if d[i] == 2:
                res[0] = i
                break
        return res