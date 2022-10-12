# Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.
# 6.78 -> 7; 5 -> нет; 0.34 -> 3

num =float(input('Введите дробное число: '))
num = num * 10 % 10
if num != 0:
    print(int(num))
else:
    print('No')



#a = float(input())
#b = int(a * 10 % 10)
#if b == 0:
#    print('no')
#print(b)


#N = float(input('Введите число N: '))
#if N % 1 == 0:
#    print("нет")
#    quit()

#N *= 10
#N = int(N % 10)

#print(N)


# a =float (input())
# b = int (a * 10 % 10)

# if a%1 == 0 :
#     b = None
# print (b)

