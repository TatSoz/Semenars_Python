# Дана последовательность чисел. Получить список уникальных (комбинация не повторяющихся цифр встречается один раз) 
# элементов заданной последовательности.
# [2, 3, 6, 1, 5, 2, 10, 3, 6, 7] -> [1, 5, 10, 7]

import random

random_list = [random.randint(1, 20) for i in range(random.randint(10, 30))]
print(random_list)
print(list(set(random_list)))