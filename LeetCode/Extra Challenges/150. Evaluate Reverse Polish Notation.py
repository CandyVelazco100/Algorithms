You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.
Evaluate the expression. Return an integer that represents the value of the expression.
  
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t in ['+', '-', '*', '/']:
                a = stack.pop()
                b = stack.pop()

                if t == '+':
                    stack.append(a+b)
                elif t == '-':
                    stack.append(b-a)
                elif t == '*':
                    stack.append(a*b)
                else:
                    stack.append(int(b/a))
            else:
                stack.append(int(t))
        return stack[0]
