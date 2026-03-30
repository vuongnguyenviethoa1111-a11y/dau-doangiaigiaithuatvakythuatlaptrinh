class Solution(object):
    def capitalizeTitle(self, title):
        """
        :type title: str
        :rtype: str
        """
        words = title.split()
        result = []
        
        for word in words:
            lower_word = word.lower()
            
           
            if len(lower_word) <= 2:
                result.append(lower_word)
            else:
                capitalized = lower_word[0].upper() + lower_word[1:]
                result.append(capitalized)
    
        return " ".join(result)