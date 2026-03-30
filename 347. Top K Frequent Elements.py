class Solution(object):
    def topKFrequent(self, nums, k):
        count = {}
        
        # Đếm số lần xuất hiện
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        
        # Sắp xếp theo tần suất giảm dần
        items = sorted(count.items(), key=lambda x: x[1], reverse=True)
        
        # Lấy k phần tử đầu
        result = []
        for i in range(k):
            result.append(items[i][0])
        
        return result
