# Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19


# list = [1.1, 1.2, 3.1, 5, 10.01]
# print(list)

from random import uniform

n = int(input('Введите размер списка '))
list = []
for i in range(n):
    f = uniform(0, 20)
    list.append(round(f, 2))
print(list)

def dif(list):
    dif_max_min =[]
    for i in range(len(list)):
        dif_max_min.append(list[i]%1)
    return max(dif_max_min) - min(dif_max_min)
print(round(dif(list),2))


