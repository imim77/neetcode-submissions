class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapa = {}
        for i, num in enumerate(nums):
            rez = mapa.get(target-num)
            if rez is None:
                mapa[num] = i
                continue
            else:
                return [rez,i]
