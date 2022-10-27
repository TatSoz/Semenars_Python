#Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
#Входные и выходные данные хранятся в отдельных текстовых файлах.
#  AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEE => 6A1F2D7C1A17E

with open('text_for_RLE.txt', 'w', encoding='UTF-8') as file:
    file.write(input('Введите текст необходимый для сжатия: '))
with open('text_for_RLE.txt', 'r') as file:
    s = file.readline()
   

def coding(txt):
    count = 1
    res = ''
    for i in range(len(txt)-1):
        if txt[i] == txt[i+1]:
            count += 1
        else:
            res = res + str(count) + txt[i]
            count = 1
    if count > 1 or (txt[len(txt)-2] != txt[-1]):
        res = res + str(count) + txt[-1]
    with open('text_compress_RLE.txt', 'w', encoding='UTF-8') as file:
        file.write(f'{res}')    
    return res

def decoding(txt):
    number = ''
    res = ''
    for i in range(len(txt)):
        if not txt[i].isalpha():
            number += txt[i]
        else:
            res = res + txt[i] * int(number)
            number = ''
    return res


print(f'Текст после кодировки: {coding(s)}')
print(f'Текст после дешифровки: {decoding(coding(s))}')