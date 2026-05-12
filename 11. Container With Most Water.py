class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l, r = 0, len(height) - 1
        res = 0
        while l < r:
            h = min(height[l], height[r])
            w = r - l
            res = max(res, h * w)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        return res