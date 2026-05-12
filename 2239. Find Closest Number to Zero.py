class Solution(object):
    def findClosestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = nums[0]
        for num in nums:
            if abs(num) < abs(res):
                res = num
            elif abs(num) == abs(res) and num > res:
                res = num
        return res