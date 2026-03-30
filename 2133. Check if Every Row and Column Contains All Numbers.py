class Solution(object):
    def checkValid(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        n = len(matrix)
        for row in matrix:
            if len(set(row)) != n:
                return False
        for c in range(n):
            column_set = set()
            for r in range(n):
                column_set.add(matrix[r][c])
            
            if len(column_set) != n:
                return False
                
        return True