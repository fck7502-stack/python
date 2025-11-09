задача 1
def f(n):
    for i in range(1, n + 1):
        if n % i == 0:
            print(i, end=" ")
num = int(input("Введите число: "))
print(f"Делители числа {num}:", end=" ")
f(num)


задача 2

def ev(a, b):
    while b:
        a, b = b, a % b
    return a

def f(num, den):
    g = ev(num, den)
    return num // g, den // g

def sub(a, b, c, d):
    num = a * d - b * c
    den = b * d
    return f(num, den)
A = int(input("Введите A: "))
B = int(input("Введите B: "))
C = int(input("Введите C: "))
D = int(input("Введите D: "))

num, den = sub(A, B, C, D)

print(f"Результат вычитания: {num}/{den}")
