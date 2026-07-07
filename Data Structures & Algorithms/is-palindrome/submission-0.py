class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(s.split()).lower()
        j = len(s)-1
        for i in range(len(s)): 
            if  not s[j].isalnum(): 
                j -= 1
            print(j)
            if not s[i].isalnum(): 
                continue
            if s[i] != s[j]:
                return False
            j -= 1
                
        return True

