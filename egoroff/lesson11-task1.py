while True:
    full_name = input('Enter full name: ')
    name_parts = full_name.split()
    for part in name_parts:
        print(part.upper())
