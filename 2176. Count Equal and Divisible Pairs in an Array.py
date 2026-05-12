class Solution(object):
    def countPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        count = 0
        for i in range(n):
            for j in range(i + 1, n):
                # Điều kiện 1: Hai số bằng nhau
                if nums[i] == nums[j]:
                    # Điều kiện 2: Tích vị trí chia hết cho k
                    if (i * j) % k == 0:
                        count += 1     
        return count