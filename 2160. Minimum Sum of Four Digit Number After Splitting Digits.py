class Solution(object):
    def minimumSum(self, num):
        """
        :type num: int
        :rtype: int
        """
        s = list(str(num))
        s.sort()
        a,b,c,d = int(s[0]),int(s[1]),int(s[2]),int(s[3])

        return 10*(a +b) + c + d
        