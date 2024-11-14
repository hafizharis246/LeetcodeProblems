from typing import List
class Solution:
    def maxAvgSubarray(self, nums: List[int], k: int) -> float:
        curr_sum = sum(nums[:k])
        max_sum = curr_sum
        for i in range(k, len(nums)):
            curr_sum = curr_sum + nums[i] - nums[i - k]
            # curr_sum +=  nums[i]
            # curr_sum -=  nums[i-k]
            max_sum = max(max_sum,curr_sum)
            
        return max_sum / k
    
    
    
s1 = Solution()
nums = [1,12,-5,-6,50,3]
k = 4
result = s1.maxAvgSubarray(nums , k)
print(result)
            
