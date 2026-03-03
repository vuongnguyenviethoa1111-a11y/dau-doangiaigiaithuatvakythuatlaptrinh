class Solution:
    def twoSum(self, nums, target):
        hashmap = {}  # Lưu số và index
        
        for i in range(len(nums)):
            need = target - nums[i]   # Số cần tìm
            
            if need in hashmap:       # Nếu đã tồn tại
                return [hashmap[need], i]
            
            hashmap[nums[i]] = i      # Lưu số hiện tại vào map