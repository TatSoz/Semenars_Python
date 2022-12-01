import logging

from telegram import ReplyKeyboardMarkup, Update
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, ConversationHandler)

from config import token
import compl
import log


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

TYPE, ACTION, NUMBERS, RESULT, MENU = range(5)

numbers_type = ''
action_type = ''


def start(update: Update, _):
    start_keyboard = [['Start']]
    markup = ReplyKeyboardMarkup(start_keyboard, one_time_keyboard=True, resize_keyboard=True)
    update.message.reply_text(f'Привет, {update.effective_user.first_name}! {chr(128075)}\n'
                              f'Я калькулятор! {chr(128425)}{chr(129299)}. Я могу работать с рациональными и комплексными числами\n'
                              f'Если Вы хотите выйти, наберите/cancel.\n\n'
                              "Начнем?",
                              reply_markup=markup)
    return TYPE


def type_numbers(update: Update, _):
    type_keyboard = [['Рациональные числа', 'Комплексные числа']]
    markup = ReplyKeyboardMarkup(type_keyboard, one_time_keyboard=True, resize_keyboard=True)
    update.message.reply_text('Выберите тип чисел, с которыми хотите работать.', reply_markup=markup)
    return ACTION


def action(update: Update, _):
    global numbers_type
    user = update.message.from_user
    log.log_type(user.first_name, update.message.text)
    numbers_type = update.message.text
    action_keyboard = [['+', '-', '*', ':', '**']]
    markup = ReplyKeyboardMarkup(action_keyboard, one_time_keyboard=True, resize_keyboard=True)
    update.message.reply_text('Выберите действие.', reply_markup=markup)
    return NUMBERS


def numbers(update: Update, _):
    global numbers_type, action_type
    log.log_operation(update.message.text)
    action_type = update.message.text
    if numbers_type == 'Рациональные числа':
        update.message.reply_text('Введите 2 числа через пробел')
    elif numbers_type == 'Комплексные числа':
        update.message.reply_text('Введите 4 числа через пробел.')
    return RESULT


def result(update: Update, _):
    global numbers_type, action_type
    reply_keyboard = [['Продолжить'], ['Выход']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True)
    nums = update.message.text
    n = nums.replace('.', '').replace(' ', '')
    numbers_list = nums.split()
    if n.isdigit() and (len(numbers_list) == 2 or len(numbers_list) == 4):
        if numbers_type == 'Рациональные числа' and len(numbers_list) == 2:
            nums = nums.replace(' ', action_type)
            result = eval(nums)
            update.message.reply_text(f'Результат {chr(128073)}: {nums}={result}\n'
                                        'Хотите продолжить?', reply_markup=markup)
            log.log_data(update.message.text)
            log.log_result(result)
            return MENU
        elif numbers_type == 'Комплексные числа' and len(numbers_list) == 4:
            result = compl.compl(nums, action_type)
            update.message.reply_text(f'Результат {chr(128073)}:' 
                                        f'{complex(int(numbers_list[0]), int(numbers_list[1]))}{action_type}{complex(int(numbers_list[2]), int(numbers_list[3]))}={result}\n'
                                        'Хотите продолжить?', reply_markup=markup)
            log.log_data(update.message.text)
            log.log_result(result)
            return MENU
        else:
            if numbers_type == 'Рациональные числа':
                update.message.reply_text(f'Некорректный ввод! {chr(9940)}\n'
                                        'Введите 2 числа через пробел.')
            elif numbers_type == 'Комплексные числа':
                update.message.reply_text(f'Некорректный ввод! {chr(9940)}\n'
                                        'Введите 4 числа через пробел.')
            return RESULT
    else:
        if numbers_type == 'Рациональные числа':
            update.message.reply_text(f'Некорректный ввод! {chr(9940)}\n'
                                      'Введите 2 числа через пробел.')
        elif numbers_type == 'Комплексные числа':
            update.message.reply_text(f'Некорректный ввод! {chr(9940)}\n'
                                      'Введите 4 числа через пробел.')
        return RESULT


def menu(update: Update, _):
    global action_type
    action_type = update.message.text
    type_keyboard = [['Рациональные числа', 'Комплексные числа']]
    markup = ReplyKeyboardMarkup(type_keyboard, one_time_keyboard=True, resize_keyboard=True)
    if action_type == 'Продолжить':
        update.message.reply_text(f"Хорошо! {chr(128077)}\n"
                                  'Выберите тип чисел, с которыми хотите работать.', reply_markup=markup)
        return ACTION
    elif action_type == 'Выход':
        update.message.reply_text(f'Пока! {chr(128521)}')
        return ConversationHandler.END


def exit(update: Update, _):
    update.message.reply_text(f'Пока! {chr(128521)}')
    return ConversationHandler.END


def main():
    updater = Updater(token, use_context=True)
    dispatcher = updater.dispatcher

    conv_handler = ConversationHandler(entry_points=[CommandHandler('start', start)],

        states={
            
            TYPE: [MessageHandler(Filters.text, type_numbers)],
            ACTION: [MessageHandler(Filters.text, action)],
            NUMBERS: [MessageHandler(Filters.text, numbers)],
            RESULT: [MessageHandler(Filters.text, result)],
            MENU: [MessageHandler(Filters.text, menu)]
        },

        fallbacks=[CommandHandler('cancel', exit)],
    )

    dispatcher.add_handler(conv_handler)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

