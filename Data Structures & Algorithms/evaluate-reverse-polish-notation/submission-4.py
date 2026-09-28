class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # add to stack until operator is seen
        # operate

        stack = []
        

        for s in tokens:
            if s not in "+*-/":
                stack.append(int(s))
            else:
                right = int(stack.pop())
                left = int(stack.pop())

                if s == "+":
                    stack.append(left + right)
                elif s == "-":
                    stack.append(left - right)
                elif s == "*":
                    stack.append(right * left)
                else:
                    stack.append(int(left / right))
        return stack[-1]