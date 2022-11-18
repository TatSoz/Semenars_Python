
import json
import controller

path_to_db = 'db.json'

def create_json():
    json_data = []
    with open(path_to_db, 'w', encoding='utf-8') as file:
        file.write(json.dumps(json_data, indent=2, ensure_ascii=False))
    controller.user_choice()


def add_to_json():
    name = input("Введите имя: ")
    surname = input('Введите Фамилию: ')
    phone = input('Введите номер телефона: ')
    comment = input('Введите коментарий: ')
    json_data = {
        "Name": name,
        "Surname": surname,
        "Phone number": phone,
        "Comment": comment,
    }
    with open(path_to_db) as file:
        data = json.load(file)
        data.append(json_data)
        
    with open(path_to_db, "w") as file:
        json.dump(data, file, indent=2, ensure_ascii=False)
    print('\nНовый контакт успешно добавлен!\n')
    controller.user_choice()

