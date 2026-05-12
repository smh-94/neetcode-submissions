class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        #start with empty stack
        stack = []
        #map every closing bracket with an opening one
        clopened = {
            '}' : '{',
            ']' : '[',
            ')' : '('
        }
        #parse through every character
        for c in s:
            #check if c is a key
            if c in clopened:
                #if we have a stack and the previous entry is equal to c's value then we pop
                if stack and stack[-1] == clopened[c]:
                    stack.pop()
                else:
                    return False
            #if it's an opening bracket, we append to the stack
            else:
                stack.append(c)
        #return True if the stack is empty, and false otherwise.
        if not stack:
            return True
        else:
            return False

#Time complexity is O(n)
#Space Complexity is O(n)