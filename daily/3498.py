class Solution:
    def reverseDegree(self, s: str) -> int:
        dict_cnt = {
            i: 0 for i in range(26, 0, -1)
        }
        alph = 'abcdefghijklmnopqrstuvwxyz'
        dict_lett = {
            alph[i]: 26 - i for i in range(len(alph))
        }

        for i in range(len(s)):
            dict_cnt[dict_lett.get(s[i])] += i + 1

        return(sum(k * v for k, v in dict_cnt.items()))
