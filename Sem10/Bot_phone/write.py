def New_Entry(file, list):
    ID = list[0]
    surname = list[1]
    # name = input('Введите имя: ')
    # father_name = input('Введите отчество: ')
    # phone = input('Введите номер телефона: ')
    # department = input('Введите отдел: ')
    # position = input('Введите должность: ')
    with open(file,'a', encoding='utf-8') as book:
        book.write(f'{ID}, {surname}\n')
        # book.write(f'{ID}, {surname}, {name}, {father_name}, {phone}, {department}, {position};\n')
  