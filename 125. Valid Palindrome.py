class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        filtered = []
        
        for c in s:
            if c.isalnum():
                filtered.append(c.lower())
        
        return filtered == filtered[::-1]