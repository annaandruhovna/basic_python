#Вывести суммы соседних элементов для ПРЯМОУГОЛЬНОЙ матрицы
#Напишите программу, на вход которой подаётся прямоугольная матрица в виде последовательности строк.
#  После последней строки матрицы идёт строка, содержащая только строку "end" (без кавычек, см. Sample Input).
# Программа должна вывести матрицу того же размера, у которой каждый элемент в позиции i, j
#  равен сумме элементов первой матрицы на позициях (i-1, j), (i+1, j), (i, j-1), (i, j+1). 
# У крайних символов соседний элемент находится с противоположной стороны матрицы.
A = []
check = True
size_i = 0
while check:
    data = input()
    if data == 'end':
        check = False
    else:
        size_i += 1
        ai = data.split()
        #Проверка размера введенных строк
        size_j = len(ai)
        if size_i > 1:
            if size_j != size_j_prev:
                break
        size_j_prev = size_j 
        ai_int = [int(i) for i in ai]
        A.append(ai_int)
if size_i != 0:         
    for i in range(size_i):
        sign =' '
        for j in range(size_j):
            if i+1 == size_i:
                i_plus = 0
            else:
                i_plus = i + 1
            if j+1 == size_j:
                j_plus = 0
                sign ='\n'
            else:
                j_plus = j + 1
            number = A[i-1][j]+ A[i_plus][j] + A[i][j-1] + A[i][j_plus]
            print(number, end=sign)