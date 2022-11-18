import json
import controller

path_to_db = 'db.json'

def export_txt():

    with open(path_to_db, 'r', encoding='utf-8') as file:
        data = json.load(file)
        for i in range(0, len(data)):
            with open('Export.txt', 'a') as export:
                export.write('\n' + "".join(data[i]['Name']) + ' ' + "".join(
                    data[i]['Surname']) + ' ' + "".join(data[i]['Phone number']) + ' ' + "".join(data[i]['Comment']))

    print('\nКонтакты успешно экспортированы в файл!\n')
    controller.user_choice()