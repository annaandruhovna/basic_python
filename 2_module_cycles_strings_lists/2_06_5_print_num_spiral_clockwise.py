#Вывод чисел от n до n^2 по возрастанию по спирали по часовой стрелке
#Выведите таблицу размером n×n, заполненную числами от 1 до n^2 по спирали,
# выходящей из левого верхнего угла и закрученной по часовой стрелке, как показано в примере (здесь n=5):
m = int(input())
A = [[0]*m for i in range(m)]
element = 1
iteration = 0
for n in range(m,1,-2):
    
    i = iteration
    for j in range(i, i+n-1, 1):
        A[i][j]=element
        element += 1
    
    j = m-iteration-1
    for i in range(iteration, j, 1):
        A[i][j]=element
        element += 1
    
    i = m-iteration-1
    for j in range(i, i-n+1, -1):
        A[i][j]=element
        element += 1

    j = iteration
    for i in range(m-iteration-1, iteration, -1):
        A[i][j]=element
        element += 1
    iteration += 1
    
if m % 2 == 1:
    c = (m-1) // 2
    A[c][c] = element
for i in range(m):
    print(*A[i])