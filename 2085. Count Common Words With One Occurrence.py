from collections import Counter

class Solution(object):
    def countWords(self, words1, words2):
        """
        :type words1: List[str]
        :type words2: List[str]
        :rtype: int
        """
        count1 = Counter(words1)
        count2 = Counter(words2)
        
        common_count = 0
        for word, freq in count1.items():
            if freq == 1:
                # Step 3: Check if that same word appeared exactly once in words2
                if count2[word] == 1:
                    common_count += 1
                    
        return common_count