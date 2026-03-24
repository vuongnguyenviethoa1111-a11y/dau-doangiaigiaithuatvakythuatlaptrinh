class Solution:
    def sortPeople(self, names, heights):

        people = []   # lưu (name, height)

        # Bước 1: ghép lại
        for i in range(len(names)):
            people.append([names[i], heights[i]])

        # Bước 2: sắp xếp giảm dần theo height
        people.sort(key=lambda x: x[1], reverse=True)

        # Bước 3: lấy lại name
        result = []
        for p in people:
            result.append(p[0])

        return result