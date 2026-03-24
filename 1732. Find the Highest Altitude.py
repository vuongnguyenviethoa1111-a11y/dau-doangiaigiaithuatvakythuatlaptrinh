class Solution:
    def largestAltitude(self, gain):

        current = 0       # Độ cao hiện tại
        maxHeight = 0     # Độ cao cao nhất

        for g in gain:

            current += g   # cộng dồn

            if current > maxHeight:
                maxHeight = current

        return maxHeight
