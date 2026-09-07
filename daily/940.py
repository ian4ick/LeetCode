class Solution:
    def distinctSubseqII(self, s: str) -> int:
        dp = 1
        last = {}

        for x in s:
            prev = dp
            dp *= 2
            if x in last:
                dp -= last[x]
            last[x] = prev

        return (dp - 1) % (10 ** 9 + 7)
