import heapq
import math
class Solution(object):
    def pickGifts(self, gifts, k):
        """
        :type gifts: List[int]
        :type k: int
        :rtype: int
        """
        # tạo max-heap bằng cách dùng số âm
        heap = [-g for g in gifts]
        heapq.heapify(heap)
        
        for _ in range(k):
            x = -heapq.heappop(heap)      # lấy lớn nhất
            x = int(math.sqrt(x))         # floor sqrt
            heapq.heappush(heap, -x)
        
        return -sum(heap)