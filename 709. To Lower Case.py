class Solution(object):
    def toLowerCase(self, s):
        result = ""

        for i in s:
            if 'A' <= i <= 'Z':
                result += chr(ord(i) + 32)
            else:
                result += i

        return result
        