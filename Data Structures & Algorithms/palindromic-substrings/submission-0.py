class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        res = 0

        def expand(l, r):
            nonlocal res
            while l >= 0 and r < n and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1

        for i in range(n):
            # odd length centers (single character center)
            expand(i, i)
            # even length centers (between i and i+1)
            expand(i, i + 1)

        return res