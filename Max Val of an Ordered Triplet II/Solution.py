from typing import List

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        prefixMax = [-1 for num in nums]
        preMax = nums[0]
        for i in range(len(nums)): 
            preMax = max(preMax, nums[i])
            prefixMax[i] = preMax

        suffixMax = [-1 for num in nums]
        sufMax = nums[-1]
        for j in range(len(nums) - 1, -1 , -1): 
            sufMax = max(sufMax, nums[j])
            suffixMax[j] = sufMax
        
        currMax = 0

        for k in range(1, len(nums) - 1): 
            value = (prefixMax[k - 1] - nums[k]) * suffixMax[k + 1]
            currMax = max(currMax, value)
        
        return currMax