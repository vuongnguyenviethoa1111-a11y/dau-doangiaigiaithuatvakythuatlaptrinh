class Solution:
    def largestAltitude(self, gain):

        current = 0       # độ cao hiện tại
        maxHeight = 0     # độ cao cao nhất

        for g in gain:

            current += g   # cộng dồn

            if current > maxHeight:
                maxHeight = current

        return maxHeight
