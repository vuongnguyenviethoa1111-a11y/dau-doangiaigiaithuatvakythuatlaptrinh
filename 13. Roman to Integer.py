class Solution(object):
    def romanToInt(self, s):
        value = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0

        for i in range(len(s)):
            # Nếu không phải ký tự cuối và ký tự hiện tại nhỏ hơn ký tự sau
            if i < len(s) - 1 and value[s[i]] < value[s[i + 1]]:
                total -= value[s[i]]
            else:
                total += value[s[i]]

        return total

        