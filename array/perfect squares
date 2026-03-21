class Solution:
    def numSquares(self, n: int) -> int:
        memo = {}
        def solve(n):
            if n == 0:
                return 0
            if n in memo:
                return memo[n]

            ans = float('inf')
            k = 1
            while k * k <= n:
                ans = min(ans, 1 + solve(n - k * k))
                k += 1

            memo[n] = ans
            return ans

        return solve(n)
