students = int(input('Введите количество учеников: '))
objects = []
for i in range(students):
    s = input('Студент ' + str(i + 1) + ': ')
    new_objects = s.strip().split()
    for new in new_objects:
        if new not in objects:
            objects += [new]
objects.sort()
print(objects)
