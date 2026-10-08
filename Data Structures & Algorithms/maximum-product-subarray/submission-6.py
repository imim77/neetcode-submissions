class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0] * n for _ in range(2)]
        
        dp[0][0] = nums[0]
        dp[1][0] = nums[0]
        
        # [3, -1, 4]
        for i in range(1, len(nums)):
            dp[0][i] = max(dp[0][i-1] * nums[i], nums[i], dp[1][i-1] * nums[i])
            dp[1][i] = min(dp[1][i-1] * nums[i], nums[i], dp[0][i-1] * nums[i])
        

        return max(dp[0])