class MinStack:

    def __init__(self):
        self.stack = []
        self.minVal = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minVal or val <= self.minVal[-1]:
            self.minVal.append(val)
    def pop(self) -> None:
        x = self.stack.pop()
        if x is self.minVal[-1]:
            y = self.minVal.pop()
        
    def top(self) -> int:
        if self.stack:
            return (self.stack[-1])
        else:
            return 0

    def getMin(self) -> int:
        return (self.minVal[-1])
