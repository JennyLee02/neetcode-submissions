class MinStack:

    def __init__(self):
        self.stack = []
        self.m = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.m:
            self.m.append(val)
        elif self.m[-1] < val:
            self.m.append(self.m[-1])
        else:
            self.m.append(val)
        

    def pop(self) -> None:
        self.stack.pop()
        self.m.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.m[-1]
        
