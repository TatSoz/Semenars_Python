import matplotlib.pyplot as plt         # вариант 1
import numpy as np

# def roots(a, b, c):
#     D = b ** 2 - 4 * a * c
#     d = D ** 0.5
#     x1 = (-b + d) / (2 * a)
#     x2 = (-b - d) / (2 * a)
#     if D > 0:
#         return x1, x2
#     elif x1 == x2:
#         return x1
#     else:
#         exit('Complex roots')

# k1, k2, k3 = 5, 10, -30

# roots = roots(k1, k2, k3)
# print(roots)

# freq = 100 # частота дискретизации типо
# a, b = -2, 2 # здесь ручками выставляем пределы по оси икс

# # квадратичная функция
# xi = np.linspace(a, b, freq)
# y = [k1 * t * t + k2 * t + k3 for t in xi]
# plt.plot(xi, y)

# plt.grid()
# plt.show()


def roots(a, b, c):
    D = b ** 2 - 4 * a * c
    d = D ** 0.5
    x1 = (-b + d) / (2 * a)
    x2 = (-b - d) / (2 * a)
    if D > 0:
        return x1, x2
    elif x1 == x2:
        return x1
    else:
        exit('Complex roots')

k1, k2, k3 = 5, 10, -30

roots = roots(k1, k2, k3)
print(roots)

list_x = list(range(-200, 0))
f = lambda x: x/100
list_x = list(map(f, list_x))
print(list_x)

f = lambda x: 5 * x * x + 10 * x - 30
list_y = list(map(f, list_x))
print(list_y)

plt.plot(list_x, list_y)
plt.show()

# 6. Определить промежутки, на котором f > 0    
# 7. Определить промежутки, на котором f < 0   

roots = list(roots)
roots.sort()
print(roots)

roots_mod = []
roots_mod.append(roots[0]-1)
roots_mod.append((roots[0]+roots[1])/2)
roots_mod.append(roots[1]+1)
print(roots_mod)

list_y_new = list(map(f, roots_mod))
print(list_y_new)

sign = lambda x: 'f>0' if x >= 0 else 'f<0'
sign = list(map(sign, list_y_new))

print(roots)
print(sign)

sign_list = []
sign_list.append(sign[0])
sign_list.append(roots[0])
sign_list.append(sign[1])
sign_list.append(roots[1])
sign_list.append(sign[2])
print(sign_list)

# 3-4 Найти интервалы, на которых функция возрастает и убывает
funct = '5x^2 + 10x - 30'
def func_to_derivative(source):

    funct = source.split()
    funct_derivative = []

    for item in funct:
        if 'x' in item:
            if '^' in item:
                temp = item.replace('x', '').split('^')

                if temp[0] == '': funct_derivative.append(temp[1] + 'x^' + str(int(temp[1]) - 1))
                else: funct_derivative.append(str(int(temp[0]) * int(temp[1])) + 'x^' + str(int(temp[1]) - 1))

            else:
                funct_derivative.append(item.replace('x', ''))

        elif '+' in item:
            funct_derivative.append('+')

        elif '-' in item:
            funct_derivative.append('-')

    if funct_derivative[-1] == '+' or funct_derivative[-1] == '-': funct_derivative.pop()
return funct_derivative