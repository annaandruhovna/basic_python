#Движение дрессированной черепашки
#Для простоты они решили считать, 
# что движение начинается в точке (0, 0), и движение на восток увеличивает первую координату,
#  а на север — вторую.Программе подаётся на вход число команд n, которые нужно выполнить черепашке,
#  после чего n строк с самими командами. Вывести нужно два числа в одну строку: 
# первую и вторую координату конечной точки черепашки. Все координаты целочисленные.
#Сумма двух листов поэлементно
def sum_on_elements(a, b):
    result = [x + y for x, y in zip(a, b)]
    return result
#Умножение листа на число поэлементно
def mult_value(a, value):
    result = [x*value for x in a]
    return result

point = [0, 0]

direct = {'север': [0, 1], 'юг': [0, -1], 'восток': [1, 0], 'запад': [-1, 0]}
count_command = int(input())
for i in range(count_command):
    command = input().split()
    dir = direct[command[0]]
    point = sum_on_elements(point, mult_value(dir,int(command[1])))
print(*point)