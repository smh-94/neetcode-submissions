class Solution:
    def addition(a,b):
        return (a+b)
    def subtraction(a,b):
        return (a-b)
    def multiplication(a,b):
        return (a * b)
    def division(a,b):
        return int(a/b)
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        a = -1
        b = -1
        for x in tokens:
            match x:
                case "+":
                    b = stack.pop()
                    a = stack.pop()
                    stack.append(Solution.addition(a,b))
                    
                case "-":
                    b = stack.pop()
                    a = stack.pop()
                    stack.append(Solution.subtraction(a,b))
                case "*":
                    b = stack.pop()
                    a = stack.pop()
                    stack.append(Solution.multiplication(a,b))
                case "/":
                    b = stack.pop()
                    a = stack.pop()
                    stack.append(Solution.division(a,b))
                case _:
                    stack.append(int(x))
        return stack.pop()