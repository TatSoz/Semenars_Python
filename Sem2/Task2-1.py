# Напишите программу, которая принимает на вход число N и выдает последовательность из N членов.
# N = 5: 1, -3, 9, -27, 81
import random

N = int(input('Введите число: '))
print(f"для N = {N}: ", end = "")

arr = []
for i in range(N):
    arr.append(random.randint(-100, 100))

print(arr)    
