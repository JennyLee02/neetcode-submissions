class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # keep the result back in the stack

        stack = []

        for token in tokens:
            if token not in "+-*/":
                stack.append(int(token))
            else:
                right = stack.pop()
                left = stack.pop()

                if token == "+":
                    res = left + right
                elif token == "-":
                    res = left - right
                elif token == "*":
                    res = left * right
                else:
                    res = int(left / right)
                stack.append(res)
        return stack[-1]