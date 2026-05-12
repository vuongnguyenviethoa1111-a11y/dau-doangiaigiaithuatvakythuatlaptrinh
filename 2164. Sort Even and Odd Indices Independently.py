class Solution(object):
    def sortEvenOdd(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        even = nums[::2]
        odd = nums[1::2]

        even.sort()
        odd.sort(reverse=True)

        res = []
        for i in range(len(even)):
            res.append(even[i])
            if i < len(odd):
                res.append(odd[i])
        
        return res
        