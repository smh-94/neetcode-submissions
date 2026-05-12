class Solution:
    def isPalindrome(self, s: str) -> bool:
        x = ''
        lowered_s = ''

        
        for y in s:
            #check if valid character
            if self.alphaNum(y):
                #take lowercase value of the character
                lowered_s += y.lower()
        #go backwards through the string
        for n in s[::-1]:
            #check if character is a valid character
            if self.alphaNum(n):
                #take the lower case value of the string 
                x += n.lower()
        return lowered_s == x 
    
    #we must check if it is a valid letter or number for it to be a palindrome
    def alphaNum (self,c):
        #ord gives the unicode to validate the ascii codes for the characters in the string
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))