class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #we compare the sorted strings and return its boolean value
        return sorted(s) == sorted(t)