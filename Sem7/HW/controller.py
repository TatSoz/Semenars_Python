
import add_contact as ac
import user_interface as ui
import change_number as cn
import change_surname as cs
import delete_contact as dc
import view_all_contact as vac
import export_contact as ec


def user_choice():

    choice_num = ui.menu()
    if choice_num < 0 or choice_num > 7:
        print('\nОшибка ввода!\n\nЧисло должно соответствовать пункту меню!\n')
        user_choice()
    elif choice_num == 0:
        ac.create_json()
    elif choice_num == 1:
        ac.add_to_json()
    elif choice_num == 2:
        cn.change_number()
    elif choice_num == 3:
        cs.change_surname()
    elif choice_num == 4:
        dc.delete_contact()
    elif choice_num == 5:
        vac.view_all_contacts()
    elif choice_num == 6:
        ec.export_txt()
    elif choice_num == 7:
        print('\nДо новых встреч!\n')
        exit()