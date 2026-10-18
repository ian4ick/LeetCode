class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        part_x = nums[:n]
        part_y = nums[n:]

        return [part_x[i // 2] if i % 2 == 0 else part_y[i // 2] for i in range(2 * n)]