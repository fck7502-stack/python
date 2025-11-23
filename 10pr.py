def f(filename):
    with open('C:\\Users\\User\\Desktop\\text.txt', 'r') as file:
        lines = file.readlines()

        n = len(lines)
        m = len(lines[0].split())
    
    A = []
    for line in lines:
        row = list(map(int, line.split()))
        A.append(row)
    
    return A, len(A), len(A[0])

def m():
    A, n, m = f('text.txt')
    
    print(f"Матрица {n}x{m}:")
    for row in A:
        print(' '.join(map(str, row)))
    
    for i in range(n):
        A[i].sort()
    
    with open('C:\\Users\\User\\Desktop\\vivod.txt', 'w') as file:
        file.write(f"{n}x{m}\n")
        for row in A:
            file.write(' '.join(map(str, row)) + '\n')
    
    print("Результат записан в 'vivod.txt'")
m()
