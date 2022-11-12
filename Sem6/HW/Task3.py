# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# A (3,6); B (2,1) -> 5,09;  A (7,-5); B (1,-1) -> 7,21

from functools import reduce

dot_A = list(map(int, input('Введите две координаты первой точки A, через пробел: ').split())) 
dot_B = list(map(int, input('Введите две координаты второй точки B, через пробел: ').split()))

def distance(dot_A, dot_B):
     rng =reduce(lambda x, y: (x + y)**(1/2), (map(lambda dot: (dot[1] - dot[0])**2, zip(dot_A, dot_B))))
     return round(rng, 2)
print(f'Расстояние между точками = {distance(dot_A, dot_B)}')
