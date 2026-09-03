"""
This solution is based on solution 3875, but it has more strict constraints.
So attempt to solve directly is not passing via time.
Math-based educational solution presented in file 3876_math.py
"""


from math import inf


class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        nums2 = [-inf] * len(nums1)
        nums2[0] = nums1[0]

        for i in range(1, len(nums1)):
            if nums1[i] % 2 == nums2[0] % 2:
                nums2[i] = nums1[i]
            else:
                for j in range(len(nums1)):
                    if j != i and (nums1[i] - nums1[j]) % 2 == nums2[0] % 2 and (nums1[i] - nums1[j]) >= 1:
                        nums2[i] = nums1[i] - nums1[j]
                        break

        simple_first_elem = -inf not in nums2
        complex_first_elem = False

        if not simple_first_elem:
            nums2 = [-inf] * len(nums1)

            for i in range(1, len(nums1)):
                if (nums1[0] - nums1[i]) % 2 != nums1[0] % 2 and (nums1[0] - nums1[i]) >= 1:
                    nums2[0] = nums1[0] - nums1[i]
                    break

            complex_first_elem_inf = nums2[0] == -inf
            if complex_first_elem_inf:
                return False

            for i in range(1, len(nums1)):
                if nums1[i] % 2 == nums2[0] % 2:
                    nums2[i] = nums1[i]
                else:
                    for j in range(len(nums1)):
                        if j != i and (nums1[i] - nums1[j]) % 2 == nums2[0] % 2 and (nums1[i] - nums1[j]) >= 1:
                            nums2[i] = nums1[i] - nums1[j]
                            break
            complex_first_elem = -inf not in nums2

        possible = simple_first_elem or complex_first_elem
        return possible