class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ['+', '-', '*', '/']
        curr = []
        for x in tokens:
            #check if x is an operator
            if x in operators:
                #if an operator, pop two and do the operation and then reinsert
                y = curr.pop()
                w = curr.pop()
                if x == '+':
                    curr.append(w + y)
                elif x == '-':
                    curr.append(w-y)
                elif x == '*':
                    curr.append(w*y)
                elif x == '/':
                    #ensure an int is appended and not a double
                    curr.append(int(w/y))
            else:
            #if it's not an operator, add it to the list as an int
                curr.append(int(x))
        return curr[-1]