# Лабораторная работа №9 “Матрицы, часть 2”
# Шагаев Андрей ИУ7-14Б
# Задача 1: Даны два одномерных целочисленных массива A и B. 
# Сформировать матрицу M, такую что 𝑚𝑖𝑗 = 𝑎𝑖 * 𝑏𝑗
# Определить количество полных квадратов в каждой строке матрицы. 
# Записать значения в массив S. Напечатать матрицу M в виде матрицы и рядом столбец S.

A = list(map(int,input("Введите элементы списка через пробел: ").split()))
while not A:
    print('Список не может быть пустым')
    A = list(map(int,input("Введите элементы списка через пробел: ").split()))

B = list(map(int,input("Введите элементы списка через пробел: ").split()))
while not B:
    print('Список не может быть пустым')
    B = list(map(int,input("Введите элементы списка через пробел: ").split()))

output_place = 0
for i in range(len(A)):
    if len(str(A[i])) > output_place:
        output_place = len(str(A[i]))
for i in range(len(B)):
    if len(str(B[i])) > output_place:
        output_place = len(str(B[i]))   
matrix = []
S=[]
for i in range(len(A)):
    row =[]
    count = 0
    for j in range(len(B)):
        el = A[i] * B[j]
        row.append(el)
        if ((el)**0.5) % 1 == 0:
            count += 1
    S.append(count)
    matrix.append(row)

for i,row in enumerate(matrix):
    for elem in row:
        print("{:>{}d}".format(elem,output_place+2),end=' ')
    print('|| ',S[i],)
print('----------------------------')

