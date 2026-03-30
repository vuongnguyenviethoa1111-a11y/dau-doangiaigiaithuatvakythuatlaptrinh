class Solution(object):
    def replaceDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        chars = list(s)
        for i in range(1, len(chars), 2):
            prev_char = chars[i-1]
            shift_amount = int(chars[i])
            
            new_char = chr(ord(prev_char) + shift_amount)
            chars[i] = new_char
            
        return "".join(chars)