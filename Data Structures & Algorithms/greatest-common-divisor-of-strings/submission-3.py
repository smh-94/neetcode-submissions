class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        res = ""
        t = ""
        for x in str1:
            t += x
            if len(str1) % len(t) == 0 and len(str2) % len(t) == 0:
                if t * (len(str1) // len(t)) == str1 and t * (len(str2) // len(t)) == str2:
                    res = t
        return res