a = int(input("Количество чисел:"))     # Считывает значение пользователя
y = 0     # Переменная которая содержит сумму чисел
for i in range(a):
    x = float(input("Введите число:"))   # Считывает числа
    y += x  # y присваевает x
y = y / a   # Вычесляет срееднее арифметическое
print(y)    # Выводит в консоль