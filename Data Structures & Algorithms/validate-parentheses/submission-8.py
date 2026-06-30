class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        for c in s:
            if c in "([{":
                stack.append(c)

            if len(stack) == 0:
                return False
            elif c == ")":
                if stack.pop() != "(":
                    return False
            elif c == "]":
                if stack.pop() != "[":
                    return False
            elif c == "}":
                if stack.pop() != "{":
                    return False
        return True if len(stack) == 0 else False
            
        