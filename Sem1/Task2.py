# Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
# 78, 55, 36, 90, 2 -> 90

#max_num = 0
#for i in range(5):
#    num = int(input(f'Введите {i + 1}-е число: '))
#    if num > max_num:
#        max_num = num
# print(max_num)



max = int(input(f'Введите 1-е число: '))
for i in range(4):
    i+=1
    N = int(input(f'Введите {i + 1}-е число: '))
    if N > max:
        max = N

print(max)