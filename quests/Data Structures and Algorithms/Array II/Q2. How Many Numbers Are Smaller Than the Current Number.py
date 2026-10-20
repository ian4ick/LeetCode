class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        res = [0] * len(nums)
        d = dict().fromkeys([i for i in range(len(nums))], [])

        for i in d.keys():
            d[i] = (nums[ : i] + nums[i + 1 : ])

        for i in d.keys():
            for j in d[i]:
                if j < nums[i]:
                    res[i] += 1

        return res