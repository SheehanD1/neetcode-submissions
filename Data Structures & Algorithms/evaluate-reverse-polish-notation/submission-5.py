class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c not in {"+", "-", "*", "/"}:
                stack.append(int(c))
            else:
                if c == "+":
                    temp = stack.pop() + stack.pop()
                    stack.append(temp)
                if c == "*":
                    temp = stack.pop() * stack.pop()
                    stack.append(temp)
                if c == "-":
                    temp = (stack.pop() - stack.pop()) * -1
                    stack.append(temp)
                if c == "/":
                    temp1 = stack.pop()
                    temp2 = stack.pop()
                    stack.append(int(temp2/temp1))
        return int(stack.pop())
                