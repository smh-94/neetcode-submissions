class MinStack:

    def __init__(self):
        self.stack = []
        #array to track older minimum numbers
        self.minVal = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        #check if val is current minumum or equal to
        if not self.minVal or val <= self.minVal[-1]:
            self.minVal.append(val)

    def pop(self) -> None:
        x = self.stack.pop()
        
        #pop current min if x is the min
        if x is self.minVal[-1]:
            y = self.minVal.pop()
        
    def top(self) -> int:
        if self.stack:
            return (self.stack[-1])
        else:
            return 0

    def getMin(self) -> int:
        return (self.minVal[-1])
