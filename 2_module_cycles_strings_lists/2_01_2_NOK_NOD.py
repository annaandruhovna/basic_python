#Нахождение НОК и НОД
#Напишите программу, которая помогает найти НОК двух чисел число.
#Программа должна считывать размеры команд (два положительных целых числа a и b,
#  каждое число вводится на отдельной строке) и выводить наименьшее число d, которое делится на оба этих числа без остатка.
a = int(input())
b = int(input())
if a >= b:
        x1 = a
        x2 = b
else:
        x1 = b
        x2 = a
check = True
while check:
    mod = x1 % x2
    if mod == 0:
        check = False
    else:
        x1 = x2
        x2 = mod
d = int(a * b / x2)
print(d)