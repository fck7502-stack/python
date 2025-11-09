Задание 2
n = int(input("Введите кол-во строк n: "))
m = int(input("Введите колво столбцов m: "))
A = []
for i in range(n):
    row = []
    for j in range(m):
        row.append(int(input(f"Введите элемент [{i},{j}]: ")))
    A.append(row)
print("Исходная матрица:")
for row in A:
    print(' '.join(map(str, row)))
for i in range(n):
    min_elem = min(A[i])
    if min_elem % 2 == 0:
        replacement = 0
    else:
        replacement = 1
    for j in range(m):
        if A[i][j] == min_elem:
            A[i][j] = replacement
            break  
print("Матрица после замены минимальных элементов:")
for row in A:

    print(' '.join(map(str, row)))

Задание 1
n = int(input("Введите кол-во строк n: "))
m = int(input("Введите кол-во столбцов m: "))
A = []
for i in range(n):
    row = []
    for j in range(m):
        row.append(int(input(f"Введите элемент [{i},{j}]: ")))
    A.append(row)
print("Исходная матрица:")
for row in A:
    print(' '.join(map(str, row)))
for i in range(n):
    A[i].sort()
print("Матрица после сортировки строк:")
for row in A:
    print(' '.join(map(str, row)))
