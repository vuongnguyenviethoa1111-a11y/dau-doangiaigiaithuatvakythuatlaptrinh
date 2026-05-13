class Solution(object):
    def pivotInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        total = n * (n + 1) // 2

        x = int(total ** 0.5)

        if x * x == total:
            return x

        return -1