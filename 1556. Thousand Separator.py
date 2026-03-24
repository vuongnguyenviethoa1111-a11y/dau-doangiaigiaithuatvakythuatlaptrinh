class Solution(object):
    def thousandSeparator(self, n):
        s = str(n)
        result = ""
        count = 0
        for i in range(len(s) - 1,-1,-1):
            count += 1
            result = s[i] + result
            
            if count == 3 and i != 0:
                result = "." + result
                count = 0
        return result