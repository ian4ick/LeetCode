class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)

        points_1 = [(r, c) for r in range(n) for c in range(n) if img1[r][c] == 1]
        points_2 = [(r, c) for r in range(n) for c in range(n) if img2[r][c] == 1]

        frequency = {}
        max_overlap = 0

        for r1, c1 in points_1:
            for r2, c2 in points_2:
                dr = r1 - r2
                dc = c1 - c2

                key = (dr, dc)
                frequency[key] = frequency.get(key, 0) + 1
                max_overlap = max(max_overlap, frequency[key])

        return max_overlap