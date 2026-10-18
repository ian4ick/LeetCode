class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        curr_cnt = 0
        max_cnt = 0

        for i in nums:
            if i == 0:
                if curr_cnt >= max_cnt:
                    max_cnt = curr_cnt
                curr_cnt = 0
            else:
                curr_cnt += 1

        if curr_cnt >= max_cnt:
            max_cnt = curr_cnt

        return max_cnt