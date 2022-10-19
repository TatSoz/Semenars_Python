# Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке некое число.
# строка (1, 4, 2, 7, 3, 10, 4, 13, 5, 16, 6, 19);   число 16 -> да

from random import sample


def find_num(length, number):
    if length <= 0:
        return "Error!"
    
    ls = sample(range(length * 2), length)
    print(ls)

    if number in ls:
        return "Yes"
    else:
        return "No"


num_1 = int(input('Enter length of the list: '))
num_2 = int(input("Enter a number: "))
print(find_num(num_1, num_2))

