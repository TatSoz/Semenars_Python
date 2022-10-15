# Реализуйте алгоритм перемешивания списка.

from random import randint

N = int(input('Введите число '))
numbers = []
for i in range(N):
    numbers.append(randint(0,N+1))
print(numbers)

list = numbers.copy()
numbers_length = len(list)
for i in range(numbers_length):
    index = randint(0, numbers_length - 1)
    temp = list[i]
    list[i] = list[index]
    list[index] = temp
print(list)

