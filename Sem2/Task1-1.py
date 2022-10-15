x = input('Введите число ')

                            
if float(x) < 0:                           
    x = float(x) * (-1)
    
    sum = 0
    for i in str(x):
        if i != '.':
            sum += int(i)

print(f'Сумма чисел равна {sum(x)}')