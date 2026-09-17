class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        n = len(arr)
        sol = n + 1
        best = n + 1

        l = -1
        sl = 0
        r = -1
        sr = 0

        for m in range(n):
            sl += arr[m]
            sr -= arr[m]

            while sl > target:
                l += 1
                sl -= arr[l]

            if sl == target:
                best = min(best, m - l)

            while r < n - 1 and sr < target:
                r += 1
                sr += arr[r]

            if sr == target:
                sol = min(sol, best + r - m)
            elif sr < target:
                break

        if sol == n + 1:
            return -1

        return sol