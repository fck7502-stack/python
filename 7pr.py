def gcd(a, b):  # Алгоритм Евклида
    while b:
        a, b = b, a % b
    return a

def simplify(num, den):  # Сокращение дроби
    g = gcd(num, den)
    return num // g, den // g

def subtract_fractions(a, b, c, d):
    num = a * d - b * c   # Вычисляем числитель
    den = b * d           # Вычисляем знаменатель
    return simplify(num, den)

# Ввод данных
A = int(input("Введите A: "))
B = int(input("Введите B: "))
C = int(input("Введите C: "))
D = int(input("Введите D: "))

num, den = subtract_fractions(A, B, C, D)
print(f"Результат вычитания: {num}/{den}")