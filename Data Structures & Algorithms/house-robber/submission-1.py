class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2: return nums[0]
        ukupno_ukradeno = [nums[0], max(nums[0], nums[1])]
        for i in range(2, len(nums)):
            opljackat_trenutnu = ukupno_ukradeno[i-2] + nums[i]
            opljackat_prethodnu = ukupno_ukradeno[i-1]

            ukupno_ukradeno.append(max(opljackat_trenutnu, opljackat_prethodnu))
        
        return ukupno_ukradeno[-1]