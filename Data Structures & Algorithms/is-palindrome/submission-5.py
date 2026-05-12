class Solution:
    def isPalindrome(self, s: str) -> bool:
        palin = ""
        reg = ""
        for x in s[::-1]:
            if (self.isAlphaNum(x)):
                palin += x.lower()
        for y in s:
            if (self.isAlphaNum(y)):
                reg += y.lower()
        print(reg)
        print(palin)
        return (reg == palin)

    def isAlphaNum(self, c) -> bool:
        return (
            ord("A") <= ord(c) <= ord("Z") or
            ord("0") <= ord(c) <= ord("9") or
            ord("a") <= ord(c) <= ord("z")
        )