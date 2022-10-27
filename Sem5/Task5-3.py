# Напишите программу, удаляющую из текста все слова, содержащие "абв".

text = 'абв авб абввв баа абв ывваабв ыукк абв'
lst1 = text.split(' ')
print(f'Исходный текст: {lst1}')
find_txt = "абв"
lst = [i for i in lst1 if find_txt not in i]
print(f'Результат: {" ".join(lst)}')        