# Напишите программу вычисления арифметического выражения заданного строкой. 
# Используйте операции +,-,/,*. приоритет операций стандартный.
# 1. 22+2*3    2. 24/2*3+30

# # 1.
# formula = '22+2*3'
# lst = []
# numbers = ''

# for i in formula:
#     if i.isdigit():
#         numbers+=i
#     else:
#         lst.append(numbers)
#         numbers=''
#         lst.append(i)
# lst.append(numbers)
# print(lst)

# for i in range(len(lst)-1, 0, -1):
#     if lst[i] == '*':
#         a = int(lst[i-1])*int(lst[i+1])
#         lst[i-1] = a
#         lst.pop(i+1)
#         lst.pop(i)
#         i-=1
#     if lst[i] == '+':
#         b = int(lst[i-1]) + int(lst[i+1])  
# print(b)

# 2.
formula = '24/2*3+30'
lst = []
numbers = ''

for i in formula:
    if i.isdigit():
        numbers+=i
    else:
        lst.append(numbers)
        numbers=''
        lst.append(i)
lst.append(numbers)
print(lst)

i = 0
while '*' in lst:
    if lst[i] == '*':
        a = int(lst[i-1])*int(lst[i+1])
        lst[i-1] = a
        lst.pop(i+1)
        lst.pop(i)
        i = 0
    else:
        i+=1
print(lst)

while '/' in lst:
    if lst[i] == '/':
        a = int(lst[i-1])/int(lst[i+1])
        lst[i-1] = a
        lst.pop(i+1)
        lst.pop(i)
        i = 0
    else:
        i+=1
print(lst)


