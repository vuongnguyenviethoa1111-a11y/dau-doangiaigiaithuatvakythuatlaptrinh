class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        paragraph = paragraph.lower()

        for c in "!?',;.":
            paragraph = paragraph.replace(c, " ")
        words = paragraph.split()

        count = {}
        for c in words:
            if c not in banned:
                if c in count:
                    count[c] += 1
                else:
                    count[c] = 1
        max_word = ""
        max_count = 0

        for c in count:
            if count[c] > max_count:
                max_count = count[c]
                max_word = c
        return max_word
        
        
        
        