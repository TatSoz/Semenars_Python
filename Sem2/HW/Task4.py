# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число

from random import randint

N = int(input('Введите число: '))

list = []
for i in range(N):
    list.append(randint(-N, N+1))

print(f'Список элементов: ', list)

f =open('file.txt','r')
poz = []
res = 1

for i in f:
    poz.append(int(i))

b = set(poz)
for i in b:
    if int(i) < len(list):
        res *= list[int(i)]

f.close()

print(f'Индексы элементов, которые надо перемножить: ', poz)
print(f'Произведение элементов на указанных позициях равно: {res}')


    



