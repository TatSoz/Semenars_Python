import delete
import write
import print1
import edit
import search
import sort
import telebot

#5803370605:AAHCc4pBsUMroUtfh4fG_HyLHSY1lfJOdd8
bot = telebot.TeleBot("5803370605:AAHCc4pBsUMroUtfh4fG_HyLHSY1lfJOdd8", parse_mode=None)

employee1 = []

@bot.message_handler(commands=['start'])   #обработчик событий (команды)
def show_Menu(message):
    bot.send_message(message.chat.id, f'Что будем делать? Выберите соответствующую цифру в меню:\n1. Вывести все записи.\n2. Добавить запись.\n3. Найти запись.\n4. Изменить запись.\n5. Удалить запись.\n6. Сортировка по ID.\n7. Выход.\n')
    #bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(content_types=["text"])      # сообщения от пользователя
def choice_user(message):
    t = message.text
    if t == '1':
        epml_list = print1.veiw_all('employees.csv')
        for i in epml_list:
            bot.send_message(message.chat.id, i)
    if t == '2':
        bot.send_message(message.chat.id, 'Введите ID')
        bot.register_next_step_handler(message, Get_ID)
        # write.New_Entry('employees.csv')
    # elif t == 3:
    #     search.Search_Entry('employees.csv')
    # elif t == 4:
    #     edit.Edit_Entry('employees.csv')
    # elif t == 5:
    #     delete.delete_str('employees.csv')
    # elif t == 6:
    #     sort.sort_data()
    # elif t == 7:
    #     print('До новых встреч!')
    
def Get_ID(message):
    IDm = message.text
    global employee1
    employee1.append(IDm)
    bot.send_message(message.chat.id, 'Введите фамилию')
    bot.register_next_step_handler(message, Get_surname)

def Get_surname(message):
    surname = message.text
    global employee1
    employee1.append(surname)
    write.New_Entry('employees.csv', employee1)
    employee1 = []
    show_Menu(message)
    bot.register_next_step_handler(message,choice_user)
    



bot.polling(non_stop=True)