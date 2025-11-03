print("Вариант 5 - Задача 1")
print("Введите 10 целых чисел:")
arr = []
for i in range(10):   
    num = int(input(f"Число {i+1}: "))  
    arr.append(num)
print("Исходный массив:", arr)
print("Пары отрицательных чисел:")
found = False
for i in range(len(arr) - 1): 
    if arr[i] < 0 and arr[i + 1] < 0: 
        print(f"Пара: ({arr[i]}, {arr[i + 1]}) на позициях {i} и {i+1}")
        found = True
if not found:    
    print("Пар отрицательных чисел нет")


print("Вариант 5 - Задача 2")
arr2 = []
for i in range(10): 
    num = int(input(f"Число {i+1}: "))
    arr.append(num)
print("Исходный массив:", arr2)
new_arr = []
for num in arr2:
    if num not in new_arr: 
        new_arr.append(num)
print("Массив без повторений:", new_arr)
