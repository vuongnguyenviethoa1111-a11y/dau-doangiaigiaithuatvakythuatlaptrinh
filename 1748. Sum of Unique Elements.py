class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        total = 0
        for num in counts:
            if counts[num] == 1:
                total += num
        
        return total