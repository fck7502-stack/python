def ev(a, b):
    while b:
        a, b = b, a % b
    return a

def g(num, den):
    g = ev(num, den)
    return num // g, den // g

def sub(a, b, c, d):
    num = a * d - b * c
    den = b * d
    return g(num, den)

# Ввод данных
A = int(input("Введите A: "))
B = int(input("Введите B: "))
C = int(input("Введите C: "))
D = int(input("Введите D: "))

num, den = sub(A, B, C, D)
print(f"Результат вычитания: {num}/{den}")