class Solution(object):
    def secondHighest(self, s):
        """
        :type s: str
        :rtype: int
        """
        digits = set()
        
        for char in s:
            if char.isdigit():
                digits.add(int(char))
        if len(digits) < 2:
            return -1
        
        sorted_digits = sorted(list(digits))
        return sorted_digits[-2]