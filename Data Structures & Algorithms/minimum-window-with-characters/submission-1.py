class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #null check
        if t == "": return ""

        countT, window = {},{}

        for c in t:
            #countT.get(c,0) --> if it exists in the map add 1 to it, otherwise add 1 to zero
            countT[c] = 1 + countT.get(c, 0)

        #we use this to track if we've reached the proper amount of valid characters in our curr string
        have, need = 0, len(countT)
        #by starting with infinity ensures that any real window length will be smaller so any first valid window will replace it
        #otherwise we return with ""
        res, resLen = [-1,-1], float("infinity")

        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c,0)

            if c in countT and window[c] == countT[c]:
                #we add to how many we have if this character exists in T and in our current window
                have += 1
            
            while have == need:
                #update our result
                if (r - l + 1) < resLen:
                    res = [l,r]
                    resLen = (r - l + 1)
                #pop from left
                window[s[l]] -= 1

                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        #return with s from l to r(accounting for off by 1 errors)
        #only return if the original length was altered
        return s[l:r + 1] if resLen != float("infinity") else ""