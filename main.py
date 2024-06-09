grades = [[5, 3, 3, 5, 4],[2, 2, 2, 3],[4, 3, 3],[4, 5, 5, 2],[5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
new_students = sorted(list(students))
print(new_students)
print(new_students[0], grades[0], sum(grades[0])/len(grades[0]))
print(new_students[1], grades[1], sum(grades[1])/len(grades[1]))
print(new_students[2], grades[2], sum(grades[2])/len(grades[2]))
print(new_students[3], grades[3], sum(grades[3])/len(grades[3]))
print(new_students[4], grades[4], sum(grades[4])/len(grades[4]))