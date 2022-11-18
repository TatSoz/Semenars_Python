import json
import controller


path_to_db = 'db.json'


def change_number():  
    name = input('Введите имя или фамилию контакта, чей номер будем менять:  ')
   
    with open(path_to_db, 'r', encoding='utf-8') as file:
        data = json.load(file)
        for i in range(0, len(data)):  
            if name == data[i]['Name'] or name == data[i]['Surname']:
                data[i]['Phone number'] = input('Новый телефон: ')
        
    with open(path_to_db, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)
    print('\nНомер успешно изменён!\n')
    controller.user_choice()