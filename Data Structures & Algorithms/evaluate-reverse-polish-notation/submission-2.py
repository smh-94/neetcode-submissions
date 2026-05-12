class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ['+', '-', '*', '/']
        curr = []
        for x in tokens:
            if x in operators:
                y = curr.pop()
                w = curr.pop()
                if x == '+':
                    curr.append(w + y)
                elif x == '-':
                    curr.append(w-y)
                elif x == '*':
                    curr.append(w*y)
                elif x == '/':
                    curr.append(int(w/y))
            else:
                curr.append(int(x))
        return curr[-1]