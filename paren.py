class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        # backtracking recursion
        out = list()
        def backtrack(pr="", l = 0, r = 0):
            #base
            if len(pr) == 2*n:
                out.append(pr)
            if l < n:
                backtrack(pr + '(', l+1, r)
            if r < l:
                backtrack(pr + ')', l, r+1)   
        backtrack()
        return out