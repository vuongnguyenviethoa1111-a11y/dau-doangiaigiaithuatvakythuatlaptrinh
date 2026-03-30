class Solution(object):
    def smallerNumbersThanCurrent(self, nums):

        out = [] 

        # sắp xếp bằng vòng for
        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)):
                if nums[j] < nums[i]: 
                    count += 1
            out.append(count)
            
        return out