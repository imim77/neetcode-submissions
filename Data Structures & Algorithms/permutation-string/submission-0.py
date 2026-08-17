class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        char_freq_arr = [0]*26
        window_size = len(s1)
        for s in s1:
            char_freq_arr[ord(s)-ord('a')] += 1
        

        l = 0
        char_freq_arr2 = [0]*26

        for r in range(len(s2)):
            char_freq_arr2[ord(s2[r]) - ord('a')] += 1
            if window_size == r-l+1:
                if char_freq_arr2 == char_freq_arr:
                    return True
                char_freq_arr2[ord(s2[l]) - ord('a')] -= 1
                l += 1
        
        return False