class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l = 0
        res = 0

        for r in range(len(s)):
            #sliding window here
            #we remove the left side from the set until s[r] is no longer in the set
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            #result the higher of the res or the 
            #length of the current difference on right and left
            res = max(res, r - l + 1)

        return res