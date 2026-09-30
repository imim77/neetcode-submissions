class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        if len(nums) == 2: return max(nums[0], nums[1])
        bez_prve = [nums[1], max(nums[1], nums[2])] 
        bez_zadnje = [nums[0], max(nums[0], nums[1])]

        for i in range(2, len(nums)-1):
            bez_prve.append(max(nums[i+1] + bez_prve[i-2], bez_prve[i-1]))

        for i in range(2, len(nums)-1):
            bez_zadnje.append(max(nums[i] + bez_zadnje[i-2], bez_zadnje[i-1]))

        print(bez_prve)
        print(bez_zadnje)
        return max(bez_prve[-1], bez_zadnje[-1])