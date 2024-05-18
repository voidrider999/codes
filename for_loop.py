offices = [
    ['john', 'sam'],
    ['peter','stu', 'miles', 'isaac'],
    ['martha', 'chloe', 'zanthia'],
]
for office in offices:
    print(str(len(office)) + ': ', end='')
    for person in office:
        print(person, end=' ')
    print()