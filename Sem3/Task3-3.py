# Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1

from random import choices


def make_words_list(count, text):
    result = []
    for i in range(count):
        el = choices(text, k=3)
        result.append("".join(el))

    return result


def find_sec_encounter(word, words_list):
    if words_list.count(word) > 1:
        first_enc = words_list.index(word)
        print(words_list.index(word, first_enc + 1))
    else:
        print(-1)


length = int(input("Enter length of the list: "))
string = input('Enter a word: ')

ls = make_words_list(length, string)

print(ls)
find_sec_encounter(input('Enter a word: '), ls)