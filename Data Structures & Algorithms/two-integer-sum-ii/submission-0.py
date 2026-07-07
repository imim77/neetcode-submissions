class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        mapa = {}
        for i in range(len(numbers)):
            res = mapa.get(target-numbers[i])
            if res is not None:
                return [res, i+1] 

            mapa[numbers[i]] = i+1
        
        return []
 