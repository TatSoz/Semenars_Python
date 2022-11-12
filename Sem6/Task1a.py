# Напишите программу вычисления арифметического выражения заданного строкой. 
# Используйте операции +,-,/,*. приоритет операций стандартный.

formula = '24/2*3+30'
lst = []
numbers = ''

def Action(array, sign):
    i = 0
    while sign in array:
        if array[i] == sign:
            if sign == '*':
                a = int(array[i-1])*int(array[i+1])
            elif sign == '/':
                a = int(array[i-1])/int(array[i+1])
            elif sign == '-':
                a = int(array[i-1])-int(array[i+1])
            elif sign == '+':
                a = int(array[i-1])+int(array[i+1])
            lst[i-1] = a
            lst.pop(i+1)
            lst.pop(i)
            i = 0
        else:
            i+=1
    return array

for i in formula:
    if i.isdigit():
        numbers+=i
    else:
        lst.append(numbers)
        numbers=''
        lst.append(i)
lst.append(numbers)
# print(lst)

i = 0
while '/' in lst or '*' in lst:
    if lst[i] == '/':
        print(Action(lst, '/'))
        i = 0
    if lst[i] == '*':
        print(Action(lst, '*'))
        i = 0
    else:
        i+=1

i = 0
while '-' in lst or '+' in lst:
    if lst[i] == '-':
        print(Action(lst, '-'))
        i = 0
    if lst[i] == '+':
        print(Action(lst, '+'))
        i = 0
    else:
        i+=1
print(lst)

# i = 0
# while '*' in lst:
#     if lst[i] == '*':
#         a = int(lst[i-1])*int(lst[i+1])
#         lst[i-1] = a
#         lst.pop(i+1)
#         lst.pop(i)
#         i = 0
#     else:
#         i+=1
# print(lst)

# while '/' in lst:
#     if lst[i] == '/':
#         a = int(lst[i-1])/int(lst[i+1])
#         lst[i-1] = a
#         lst.pop(i+1)
#         lst.pop(i)
#         i = 0
#     else:
#         i+=1
# print(lst)


