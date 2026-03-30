class Solution(object):
    def destCity(self, paths):
         for i in range(len(paths)):
        
            cityB = paths[i][1]
            found = False
            for j in range(len(paths)):
                if cityB == paths[j][0]:
                    found = True
                    break

            if found == False:
                return cityB






        