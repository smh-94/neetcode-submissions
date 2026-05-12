class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        res = 0

        def expand(l, r):
            nonlocal res
            #we check if l and r are in bounds and are the same characters before expanding
            #if the boolean passes, then we iterate the result
            while l >= 0 and r < n and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1

        for i in range(n):
            # odd length centers (single character center)
            # Finds solutions in AAA 'a'a'a'
            expand(i, i)
            #finds solutions 'aa' 'aa' in AAA
            # even length centers (between i and i+1)
            expand(i, i + 1)

        return res