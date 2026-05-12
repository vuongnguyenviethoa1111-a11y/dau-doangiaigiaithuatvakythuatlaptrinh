class Solution(object):
    def mostFrequent(self, nums, key):
        """
        :type nums: List[int]
        :type key: int
        :rtype: int
        """
        count = {}   # đếm tần suất
        for i in range(len(nums) - 1):

            if nums[i] == key:

                next_num = nums[i + 1]

                if next_num in count:
                    count[next_num] += 1
                else:
                    count[next_num] = 1
        max_count = 0
        result = 0
        for k in count:
            if count[k] > max_count:
                max_count = count[k]
                result = k

        return result