# Найдите корни квадратного уравнения Ах^2 + Вх + С = 0

from math import sqrt

a = int(input("Enter A: "))
b = int(input("Enter B: "))
c = int(input("Enter C: "))

D = b ** 2 - 4 * a * c
print(D)
if D > 0:
    x1 = ((-b + sqrt(D)) / (2 * a))
    x2 = ((-b - sqrt(D)) / (2 * a))
    print(f'x1 = {round(x1, 2)}, x2 = {round(x2, 2)}')
elif D == 0:
    x = (-b / (2 * a))   
    print(x)
else:
    print('корней нет')
