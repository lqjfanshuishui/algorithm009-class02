# Leetcode 1. Two sum : find two numbers in an array if their sum is equal to the target

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res_dict = {}
        for i in range(len(nums)):
            if target - nums[i] in res_dict:
                return [res_dict[target - nums[i]], i]
            else:
                res_dict[nums[i]] = i
        return -1
