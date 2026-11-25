class MinStack:

    
    def __init__(self):
        
        self.stack = []

    def push(self, val: int) -> None:
        
        self.stack.append(val)

    def pop(self) -> None:
        self.stack = self.stack[:len(self.stack) - 1]


    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        if self.stack:
            m = self.stack[0]
            for e in self.stack:
                if e < m:
                    m = e
            return m
        
        return None
