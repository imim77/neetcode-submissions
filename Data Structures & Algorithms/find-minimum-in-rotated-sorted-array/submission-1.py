class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        najmanji = float('inf')

        while(l <= r):
            mid = l+(r-l)//2
            najmanji = min(najmanji, nums[mid])
            if(nums[mid] > nums[r]):
                l = mid+1
            else:
                r = mid-1
        
        return najmanji