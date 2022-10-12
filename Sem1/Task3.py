# Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N

#num =int(input('Введите число: '))
#print(*range(-num, num + 1))



# N = int(input('Введите число N: '))
# N = abs(N)

# for i in range(-N, N+1):
#    print(i, end=', ')
# print(N)

N = int(input('Введите число N: '))
N = abs(N)

i = -N
while i < N:
    print(i, end=', ')
    i += 1
print(N)

