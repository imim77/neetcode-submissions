class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mapa = {}
        for num in nums:
            if num in mapa:
                return True
            mapa[num] = "postoji"
        return False