# Напишите программу, которая принимает на вход цифру, 
# обозначающую день недели, и проверяет, является ли этот день выходным.
# 7 -> да;  1 -> нет

num =int(input('Введите число: '))
if 1 <= num <= 5:
    print('Рабочий день')
elif num == 6 or num == 7:
    print('Выходной день')
else:
    print('Такого дня недели не существует')