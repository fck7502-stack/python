def read_matrix_flexible(filename):
    """Чтение матрицы с автоматическим определением размеров"""
    with open('C:\\Users\\User\\Desktop\\text.txt', 'r') as file:
        lines = file.readlines()
        
        # Если первая строка содержит только 2 числа - это размеры
        first_line = lines[0].split()
        if len(first_line) == 2 and all(x.isdigit() for x in first_line):
            n, m = map(int, first_line)
            start_index = 1
        else:
            # Размеры не указаны, определяем автоматически
            n = len(lines)
            m = len(lines[0].split())
            start_index = 0
        
        A = []
        for i in range(start_index, start_index + n):
            if i < len(lines):
                row = list(map(int, lines[i].split()))
                A.append(row)
    
    return A, len(A), len(A[0]) if A else 0

def main_flexible():
    A, n, m = read_matrix_flexible('input.txt')
    
    print(f"Матрица {n}x{m}:")
    for row in A:
        print(' '.join(map(str, row)))
    
    # Сортировка строк
    for i in range(n):
        A[i].sort()
    
    # Запись в файл
    with open('C:\\Users\\User\\Desktop\\vivod.txt', 'w') as file:
        file.write(f"Матрица {n}x{m} после сортировки строк:\n")
        for row in A:
            file.write(' '.join(map(str, row)) + '\n')
    
    print("Результат записан в 'output.txt'")

# Запуск
main_flexible()