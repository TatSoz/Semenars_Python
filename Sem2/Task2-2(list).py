#  Получить список чисел. Превратите его в список квадратов этих чи


import random
N = 10
list1 = []
for i in range(N):
    list1.append(random.randint(0, 50))
print(list1)

for i in range(len(list1)):
    list1[i] = list1[i] * list1[i]

print(list1)
