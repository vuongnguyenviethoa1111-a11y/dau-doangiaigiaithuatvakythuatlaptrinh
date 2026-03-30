class Solution(object):
    def heightChecker(self, heights):

        expected = heights[:]  # copy mảng

        n = len(expected)

        # sắp xếp bằng 2 vòng for
        for i in range(n):
            for j in range(n - 1):
                if expected[j] > expected[j + 1]:
                    temp = expected[j]
                    expected[j] = expected[j + 1]
                    expected[j + 1] = temp

        count = 0

        for i in range(n):
            if heights[i] != expected[i]:
                count += 1

        return count