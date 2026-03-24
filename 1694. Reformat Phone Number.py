class Solution:
    def reformatNumber(self, number):

        # Bước 1: bỏ ký tự không phải số
        digits = ""
        for c in number:
            if c.isdigit():
                digits += c

        res = []
        i = 0
        n = len(digits)

        # Bước 2: chia nhóm
        while n - i > 0:

            if n - i > 4:
                res.append(digits[i:i+3])
                i += 3

            elif n - i == 4:
                res.append(digits[i:i+2])
                res.append(digits[i+2:i+4])
                break

            else:
                res.append(digits[i:])
                break

        return "-".join(res)