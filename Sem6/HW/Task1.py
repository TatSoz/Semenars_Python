# Напишите программу, удаляющую из текста все слова, содержащие "абв".

text = 'абв авб абввв азбука абвгдейка баа абв ывваабв ыукк абв'
result = ' '.join(filter(lambda x: "абв" not in x, text.split()))
print(result)
