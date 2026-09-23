class Solution:
    def climbStairs(self, n: int) -> int:
        # dp je broj razlicitih nacina da se popnem na i-tu stepenicu
        # znaci ako se zelim popeti na prvu stepenicu to mogu samo ako napravim 1 korak
        # ako se zelim popesti na drugu stepenicu mogu napraviti ili 1+1 korak ili 2 koraka odmah
        # ako se zelim popesti na trecu stepenicu onda mogu ili 1+1+1 ili 2+1 ili 1+2
        if n == 1:
            return 1
        dp = [1,2]
        for i in range(2, n):
            dp.append(dp[i-1]+dp[i-2])

        return dp[-1]