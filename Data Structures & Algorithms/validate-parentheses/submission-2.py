class Solution:
    def isValid(self, s: str) -> bool:
        validParenthesis = {'(':')',
                            '{':'}',
                            '[':']'}
        stack = []
        #we need to check if a closing bracket is closing the correct open bracket in the stack
        for i in range(len(s)):
            #case 1, no stack exists
            #case 2, closing parenthesis with valid parenthesis
            #case 3, new opening parenthesis
            #case 4, invalid parenthesis
            if not stack:
                if s[i] in validParenthesis:
                    stack.append(s[i])
                else:
                    return False
            elif validParenthesis[stack[-1]] == s[i]:
                stack.pop()
            elif s[i] in validParenthesis:
                stack.append(s[i])
            else:
                return False
        if stack:
            return False
        return True