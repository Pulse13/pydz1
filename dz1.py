# 1) Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

daynumber = int(input('Введите число от 1 до 7\n'))
if daynumber > 5:
    print('yes')
else:
    print('no')

# 2) Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

X = input('X = ')
Y = input('Y = ')
Z = input('Z = ')
leftside = not(X and Y and Z)
rightside = not X or not Y or not Z
print(leftside == rightside)

# 3) Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

xy = [int(input('x = ')), int(input('y = '))]
if (xy[0] != 0 or xy[1] != 0):
    if xy[0] > 0 and xy[1] > 0:
        print('1ая четверть')
    if xy[0] > 0 and xy[1] < 0:
        print('4ая четверть')
    if xy[0] < 0 and xy[1] > 0:
        print('2ая четверть')
    if xy[0] < 0 and xy[1] < 0:
        print('3ая четверть')
    if xy[0] == 0:
        print('ось Y')
    if xy[1] == 0:
        print('ось X')

# 4) Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

partNumber = int(input('Введите число от 1 до 4\n'))
if partNumber == 1:
    print('Х > 0 ; Y > 0')
if partNumber == 2:
    print('Х < 0 ; Y > 0')
if partNumber == 3:
    print('Х < 0 ; Y < 0')
if partNumber == 4:
    print('Х > 0 ; Y < 0')

# 5) Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

import math

xy1 = [int(input('x1 = ')), int(input('y1 = '))]
xy2 = [int(input('x2 = ')), int(input('y2 = '))]
result = math.sqrt((xy2[0]-xy1[0])**2 + (xy2[1]-xy1[1])**2)
print(result)