class Solution:
    def findNumbers(self, nums):

        count = 0   # đếm kết quả

        for num in nums:

            length = len(str(num))   # chuyển sang string để đếm

            if length % 2 == 0:      # nếu chẵn
                count += 1

        return count