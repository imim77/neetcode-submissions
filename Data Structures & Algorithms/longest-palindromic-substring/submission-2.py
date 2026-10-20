class Solution:
    def longestPalindrome(self, s: str) -> str:
        resLen, resIndex = 0, 0

        n = len(s)

        dp = [[False] * n for _ in range(n)]

        for i in range(n-1, -1, -1):
            for j in range(i, n):
                # Ovaj prvi uvjet je ako je substring neparan, jer ako su s[i] == s[j] onda je sikak palindrome,
                # a ako imamo "abba" npr. onda nije dosta da samo usporedimo a i a nego onda tu dolazi i ovaj drugi
                # uvjet koji nam govori ako su i njegovi susjedni elementi isti e onda je palindrome
                if s[i] == s[j] and (j-i <= 2 or dp[i+1][j-1]):
                    dp[i][j] = True
                    if resLen < (j-i+1):
                        resLen = j-i+1
                        resIndex = i
        
        return s[resIndex : resIndex + resLen]