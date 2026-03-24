class Solution:
    def areOccurrencesEqual(self, s):

        count = {}   # dictionary để đếm

        # Bước 1: đếm ký tự
        for c in s:
            if c in count:
                count[c] += 1
            else:
                count[c] = 1

        # Bước 2: lấy số lần của ký tự đầu tiên
        values = list(count.values())
        first = values[0]

        # Bước 3: so sánh
        for v in values:
            if v != first:
                return False

        return True