class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        count_ab = {}

        #Bước 1:tình tổng nums1 + nums2
        for a in nums1:
            for b in nums2:
                s = a + b
                count_ab[s] = count_ab.get(s,0) + 1
        total = 0

        #bước 2: Kiểm Tra nums3 + nums4 
        for c in nums3:
            for d in nums4:
                s += c + d
                total += count_ab.get(-(c + d),0)
        
        return total
        