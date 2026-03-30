class Solution(object):
    def distributeCandies(self, candyType):
        n = len(candyType)
        half = n // 2

        distinct = len(set(candyType))

        return min(distinct, half)