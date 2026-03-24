class Solution:
    def countBalls(self, lowLimit, highLimit):

        box = {}   # lưu số bóng trong từng hộp

        # duyệt từng quả bóng
        for num in range(lowLimit, highLimit + 1):

            # tính tổng chữ số
            s = 0
            temp = num

            while temp > 0:
                s += temp % 10
                temp //= 10

            # tăng số bóng trong hộp s
            if s in box:
                box[s] += 1
            else:
                box[s] = 1

        # tìm max
        maxBall = 0
        for v in box.values():
            if v > maxBall:
                maxBall = v
        return maxBall