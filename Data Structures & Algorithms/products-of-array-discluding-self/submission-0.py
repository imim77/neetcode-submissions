class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            j = 0
            product = 1
            while j<len(nums):
                if i == j:
                    j += 1
                    continue
                else:
                    product *= nums[j]
                    j +=1
            
            res.append(product)
        
        return res