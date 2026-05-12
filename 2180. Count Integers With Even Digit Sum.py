class Solution(object):
    def countEven(self, num):
        """
        :type num: int
        :rtype: int
        """
        temp_num = num
        tong_chu_so_cua_num = 0
        while temp_num > 0:
            tong_chu_so_cua_num += temp_num % 10
            temp_num //= 10
        if tong_chu_so_cua_num % 2 == 0:
            return num // 2
        else:
            return (num - 1) // 2