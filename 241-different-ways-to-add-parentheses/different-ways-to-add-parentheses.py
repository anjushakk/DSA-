class Solution:
    def diffWaysToCompute(self, expression: str):
        memo = {}

        def ways(expr):
            # If already computed, return stored result
            if expr in memo:
                return memo[expr]

            res = []
            # Split at every operator
            for i, ch in enumerate(expr):
                if ch in '+-*':
                    left = ways(expr[:i])
                    right = ways(expr[i+1:])

                    # Combine all left and right results
                    for l in left:
                        for r in right:
                            if ch == '+':
                                res.append(l + r)
                            elif ch == '-':
                                res.append(l - r)
                            else:  # '*'
                                res.append(l * r)

            # Base case: if expr is just a number
            if not res:
                res.append(int(expr))

            memo[expr] = res
            return res

        return ways(expression)
