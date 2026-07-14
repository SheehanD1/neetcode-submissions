class MinStack:

    def __init__(self):
        self.stack = []
        self.minVals = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minVals[-1] if self.minVals else val)
        self.minVals.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minVals.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minVals[-1]
