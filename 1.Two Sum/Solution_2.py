class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        indexdict = {}
        for i in range(len(nums)):
            if target - nums[i] in indexdict:
                return [indexdict[target - nums[i]],i]
            indexdict[nums[i]] = i
        return []
            
            