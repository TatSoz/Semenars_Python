# Дан список чисел. Создайте список, в который попадают числа, 
# описываемые возрастающую последовательность. Порядок элементов менять нельзя.
# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.

lst = [1, 5, 2, 3, 4, 6, 1, 7]

list_new = [lst[0]]
min = list_new[0]
for i in range(1, len(lst)):
    if lst[i] > min:
        list_new.append(lst[i])
        min = list_new[-1]
print(list_new)

# list_new = [lst[0]]
# min = lst[0]
# for i in range(1, len(lst)):
#     if lst[i] > min:
#         list_new.append(lst[i])
#         min = lst[i]
# print(list_new)