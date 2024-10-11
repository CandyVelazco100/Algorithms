Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(s, openP, closeP):
            if n == openP == closeP:
                res.append(s)
                return
            
            if openP < n:
                backtrack(s + '(', openP+1, closeP)
            
            if closeP < openP:
                backtrack(s + ')', openP, closeP+1)
                
        backtrack('', 0, 0)
        return res
