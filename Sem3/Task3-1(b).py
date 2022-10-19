# Реализовать создание списка случайных элементов - строк

import datetime

mas = list(map(chr, range(97, 123)))  # преобразуем коды букв в буквы, и создаем массив
print(mas)
n=15
b1=0
b2=25
a = (datetime.datetime.now() - datetime.datetime(1, 1, 1, 0, 0)).total_seconds()
a=a%1
s=''
for i in range (10):
    a = a*(datetime.datetime.now() - datetime.datetime(1, 1, 1, 0, 0)).total_seconds()
    a=(a*1000)%1
    #sleep(1)
    print(a)
    stroka=mas[round(b1+(b2-b1)*a)]
    s+=stroka
print(s)


