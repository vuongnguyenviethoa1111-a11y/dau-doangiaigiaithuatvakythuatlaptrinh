class Solution:
    def sortPeople(self, names, heights):

        people = []   # lưu (name, height)
        for i in range(len(names)):
            people.append([names[i], heights[i]])
        people.sort(key=lambda x: x[1], reverse=True)
        result = []
        for p in people:
            result.append(p[0])

        return result