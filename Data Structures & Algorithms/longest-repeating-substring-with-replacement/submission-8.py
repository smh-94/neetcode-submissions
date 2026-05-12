class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        res = 0
        alph = {}
        maxF = 0
        for r in range(len(s)):
            #increase the value in the map
            if s[r] not in alph:
                alph[s[r]] = 1
            else:
                alph[s[r]] += 1
            maxF = max(alph.values())
            #shrink window
            while r - l + 1 - maxF > k:
                #subtract 1 from the key's value's count
                alph[s[l]] -= 1
                #recalculate maxF because the character count at l might have been the maxF
                maxF = max(alph.values())
                #shift left
                l += 1
            res = max(r - l + 1,res)
        return res
