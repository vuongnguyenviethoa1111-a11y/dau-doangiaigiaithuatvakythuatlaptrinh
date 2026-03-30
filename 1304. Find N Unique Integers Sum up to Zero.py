class Solution(object):
    def sumZero(self, n):
         
        out = []

        for i in range(1, n / 2+1):
            out.append(i)
            out.append(-i)

        if n % 2 == 1:
            out.append(0)
        
        return out

        