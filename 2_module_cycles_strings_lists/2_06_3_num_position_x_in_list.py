#Вывод всех позиций числа в листе
#Напишите программу, которая считывает список чисел lst из первой строки и число x из второй строки,
# которая выводит все позиции, на которых встречается число x в переданном списке lst.
#Позиции нумеруются с нуля, если число x не встречается в списке, 
# вывести строку "Отсутствует" (без кавычек, с большой буквы).
# Позиции должны быть выведены в одну строку, по возрастанию абсолютного значения.
lst = input().split()
x = input()
nums = []
if x in lst:
    while x in lst:
        num = lst.index(x)
        nums.append(num)
        lst[num] = 'check'
    print(*nums)
else:
    print('Отсутствует')