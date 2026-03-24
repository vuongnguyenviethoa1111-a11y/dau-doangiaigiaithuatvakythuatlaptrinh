class Solution:
    def distributeCandies(self, candies, num_people):

        res = [0] * num_people   # tạo mảng kết quả
        i = 1                    # số kẹo sẽ phát
        index = 0                # người hiện tại

        while candies > 0:

            if candies >= i:
                res[index] += i
                candies -= i
            else:
                res[index] += candies
                break

            i += 1
            index += 1

            if index == num_people:
                index = 0   # quay lại đầu

        return res