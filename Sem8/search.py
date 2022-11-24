def Search_Entry(file):

    print(f'Введите элемент имени сотрудника для поиска в БД: ')
    name = input()
   
    with open(file, 'r', encoding="utf-8") as data:
            for line in data:
                if name in line: 
                    print(line)
                    break
                else:
                    print("Incorrect entry! Please, choose something from the list!")

            
       
               