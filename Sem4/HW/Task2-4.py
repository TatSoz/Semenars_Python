# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def factors(number):
    result = []
    i = 2

    while number > 1:
        if number % i == 0:
            result.append(i)
            number //= i
        else:
            i += 1
    
    return result


num = int(input('Введите число: '))
print(factors(num))


