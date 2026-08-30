class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        maximum = nums[0]
        minimum = nums[0]
        maximum_ind = 0
        minimum_ind = 0

        if len(nums) == 1 or len(nums) == 2:
            return len(nums)

        for i in range(1, len(nums)):
            if nums[i] > maximum:
                maximum = nums[i]
                maximum_ind = i
            if nums[i] < minimum:
                minimum = nums[i]
                minimum_ind = i

        minimum_positions_left = len(nums[:minimum_ind]) + 1
        maximum_positions_left = len(nums[:maximum_ind]) + 1
        minimum_positions_right = len(nums[-1:minimum_ind - len(nums):-1]) + 1
        maximum_positions_right = len(nums[-1:maximum_ind - len(nums):-1]) + 1

        general_left = max(minimum_positions_left, maximum_positions_left)
        general_right = max(minimum_positions_right, maximum_positions_right)

        return min(general_left, general_right, minimum_positions_left + maximum_positions_right,
                   maximum_positions_left + minimum_positions_right)