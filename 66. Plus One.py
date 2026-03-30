class Solution(object):
    def plusOne(self, digits):
        # Duyệt từ cuối mảng về đầu
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0

        # Nếu tất cả chữ số đều là 9
        return [1] + digits
