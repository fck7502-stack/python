n = int(input("Введите натуральное число n: "))
sum_cubes = 0

for i in range(1, n + 1):
    sum_cubes += i ** 3

print("сумма кубов от 1 до", n, "равна:", sum_cubes)




N = int(input("введите количество чисел из ряда Фибоначчи (N): "))
K = int(input("введите номер в ряду, с которого начать (K): "))
a = 0
b = 1
fib_sum = 0
count = 0
for i in range(1, K):
    a, b = b, a + b
while count < N:
    fib_sum += b
    a, b = b, a + b
    count += 1
print("сумма", N, "чисел Фибоначчи, начиная с", K, "-го, равна:", fib_sum)
