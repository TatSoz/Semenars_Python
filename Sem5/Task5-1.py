# В файле находится N натуральных чисел, записанных через пробел. 
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.

with open('filefor5_1.txt') as f:
    str1 = f.read()

lst = str1.split(' ')
# print(lst)

for i in range(len(lst)):
    lst[i] = int(lst[i])

print(lst)

for i in range(1, len(lst)):
    if lst[i] != lst[i-1] + 1:
        print(lst[i-1] + 1)
        break