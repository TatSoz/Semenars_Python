import json
import controller

path_to_db = 'db.json'


def change_surname():
    name = input(
        'Введите имя или фамилию контакта, фамилию которого будем менять:  ')

    with open(path_to_db, 'r', encoding='utf-8') as file:
        data = json.load(file)
        for i in range(0, len(data)):
            if name == data[i]['Name'] or name == data[i]['Surname']:
                data[i]['Surname'] = input('Новая фамилия: ')
        
    with open(path_to_db, 'w', encoding='utf') as file:
        json.dump(data, file, indent=4)
    print('\nФамилия успешно изменена!\n')
    controller.user_choice()