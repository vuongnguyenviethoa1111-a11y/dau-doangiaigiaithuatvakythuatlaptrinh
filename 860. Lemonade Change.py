class Solution:
    def lemonadeChange(self, bills):

        five = 0      # số tờ 5$ đang có
        ten = 0       # số tờ 10$ đang có

        for b in bills:   # duyệt từng khách trong hàng

            if b == 5:    
                # khách trả đúng 5$, không cần thối tiền
                five += 1   # thêm 1 tờ 5 vào ví

            elif b == 10:
                # khách trả 10$, phải thối lại 5$
                if five == 0:
                    return False   # không có 5$ để thối → fail

                five -= 1   # đưa 1 tờ 5 cho khách
                ten += 1    # nhận 1 tờ 10 từ khách

            else:  # b == 20
                # khách trả 20$, phải thối 15$

                if ten > 0 and five > 0:
                    # ưu tiên trả 10 + 5
                    ten -= 1
                    five -= 1

                elif five >= 3:
                    # nếu không có 10 thì dùng 3 tờ 5
                    five -= 3

                else:
                    # không đủ tiền thối
                    return False

        return True   # tất cả khách đều thối được