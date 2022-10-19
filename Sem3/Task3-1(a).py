# Реализуйте алгоритм задания случайных чисел без использования встроенного генератора псевдослучайных чисел.
#Реализовать создание списка случайных элементов

import datetime
b1=10
b2=20
a = (datetime.datetime.now() - datetime.datetime(1, 1, 1, 0, 0)).total_seconds()
a=a%1
print(a)
new=round(b1+(b2-b1)*a)
print(new)
