class Solution:
    def isPalindrome(self, s: str) -> bool:
        x = ''
        lowered_s = ''
        for y in s:
            if self.alphaNum(y):
                lowered_s += y.lower()
        for n in s[::-1]:
            if self.alphaNum(n):
                x += n.lower()
        return lowered_s == x 
    
    
    def alphaNum (self,c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))