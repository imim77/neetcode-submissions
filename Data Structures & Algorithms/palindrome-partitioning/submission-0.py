class Solution:
    def isPalindrome(self, s, i, j):
        l = i
        r = j
        while l<r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

    def partition(self, s: str) -> List[List[str]]:
        res = []

        def dfs(i, j, path):
            if i >= len(s):
                res.append(path.copy())
                return
            
            if j >= len(s):
                return
            
            dfs(i, j+1, path)

            if self.isPalindrome(s, i, j):
                path.append(s[i:j+1])
                dfs(j+1,j+1, path)
                path.pop()

        dfs(0,0,[])
        return res