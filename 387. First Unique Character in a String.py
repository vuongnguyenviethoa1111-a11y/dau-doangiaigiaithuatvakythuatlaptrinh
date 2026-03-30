class Solution(object):
    def firstUniqChar(self, s):
        count = {}

        # Đếm số lần xuất hiện của từng ký tự
        for ch in s:
            if ch in count:
                count[ch] += 1
            else:
                count[ch] = 1

        # Tìm ký tự đầu tiên xuất hiện đúng 1 lần
        for i in range(len(s)):
            if count[s[i]] == 1:
                return i

        return -1