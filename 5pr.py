s = input('Введите строку: ')
for word in s.split():
    if word[-1] == 'я': print(word)