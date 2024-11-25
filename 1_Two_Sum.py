from typing import List
class Solution:
    def twoSum(self, nums:List[int], target: int) -> List[int]:

    # 1st- Way in which we are retrieving the indices by saving it in values in dictionary and the values are its keys equal to target
    #     dict = {}
    #     for i, num in enumerate(nums):
    #         compliment = target - num

    #         if compliment in dict:
    #             return [i, dict[compliment]]

    #         dict[num] = i
    #     # It is given in Program that it will have answer. If by chance it doesn't contains answer then it will give this
    #     return None

    # 2nd- Way in which we retieve the keys as indices from the dictionary which is equals to target
        # dict = {}
        # for i, num in enumerate(nums):
        #     compliment = target - num

        #     if compliment in dict.values():
        #         compliment_index = [key for key, value in dict.items() if value == compliment][0]
        #         return [compliment_index, i]

        #     dict[i] = num

        # return None

    # 3rd- Way in which we use the looping without the dictionary
    # This way is more space complexity because it uses the nested loops 
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return[i,j]

        return None



s1 = Solution()
target = 9
nums = [2,7,11,15]
result = s1.twoSum(nums, target)
print(result)
