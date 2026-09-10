class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def backtrack(path, i):
            if path not in res:
                res.append(path.copy())

            if i == len(nums):
                return

            path.append(nums[i])
            backtrack(path, i+1)
            path.pop()

            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            backtrack(path, i+1)
        
        backtrack([], 0)
        return res