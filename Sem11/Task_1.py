# Дана функция f(x) = 5x^2 + 10x - 30
# Определить корни

a = float(input('Введите a: '))
b = float(input('Введите b: '))
c = float(input('Введите c: '))

D = b**2 - 4 * a * c

if (D > 0):
x1 = (math.sqrt(D) - b) / (2 * a)
x2 = (-math.sqrt(D) - b) / (2 * a)
print(f'x1 = {x1}, x2 = {x2}')
elif (D == 0):
x = (-b / 2* a)
print(f'x = {x}')
else:
print('Корней в уравнении нет')