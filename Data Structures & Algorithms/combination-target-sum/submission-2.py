class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(i, subarr, total):
            if total == target:
                res.append(subarr.copy())
                return
            
            if i >= len(nums) or total > target:
                return
            
            subarr.append(nums[i])
            backtrack(i, subarr, total + nums[i])
            subarr.pop()
            
            # not including nums[i]
            backtrack(i+1, subarr, total)

           
        backtrack(0, [], 0)
        return res