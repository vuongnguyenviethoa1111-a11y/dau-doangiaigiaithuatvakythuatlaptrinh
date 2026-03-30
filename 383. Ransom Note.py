class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        # Tạo dictionary để đếm số lần xuất hiện của chữ trong magazine
        count = {}
        
        # Đếm từng ký tự trong magazine
        for ch in magazine:
            if ch in count:
                count[ch] += 1
            else:
                count[ch] = 1
        
        # Duyệt từng ký tự trong ransomNote
        for ch in ransomNote:
            # Nếu chữ không tồn tại hoặc đã dùng hết
            if ch not in count or count[ch] == 0:
                return False
            else:
                # Dùng 1 chữ thì giảm số lượng đi 1
                count[ch] -= 1
        
        # Nếu dùng được hết chữ trong ransomNote
        return True

        