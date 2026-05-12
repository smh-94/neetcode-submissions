class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return len(s)
        m = 0
        for i  in range(len(s)):
            n = [s[i]]
            for j in range(i+1,len(s),1):
                if s[j] not in n:
                    n.append(s[j])
                else:
                    break
            if len(n) > m:
                m = len(n)
        return m 