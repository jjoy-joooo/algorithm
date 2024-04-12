gems = [3, 3, 1, 2, 3, 22, 3, 3, 1, 77]
grades = {}

for i in gems:
    grades[i] = grades.get(i, 0) + 1

    # if grades.get(i, -1) == -1:
    #     grades[i] = 1
    # else:
    #     grades[i] = grades[i] + 1

print(grades)
