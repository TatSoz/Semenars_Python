def New_Entry():
    ID = input('Введите ID: ')
    surname = input('Введите фамилию: ')
    name = input('Введите имя: ')
    father_name = input('Введите отчество: ')
    phone = input('Введите номер телефона: ')
    department = input('Введите отдел: ')
    position = input('Введите должность: ')
    with open('employees.csv','a', encoding='utf-8') as book:
        book.write(f'{ID}, {surname}, {name}, {father_name}, {phone}, {department}, {position};\n')

