nums = int(input())     # Количество чисел
listnums = []   # Готовый пустой список
for i in range(nums):
    listnums.append(int(input()))   # Добовляет числа в пустой список
for i in range(nums):
    if listnums[i] % 5 == 0:    # Выевляет числа из списка кратные 5
        listnums[i] = listnums[i] // 5 * 2  # Делит нацело на 5 и умнажает на 2
    elif listnums[i] % 2 == 0:  # Выевляет числа из списка кратные 2
        listnums[i] = listnums[i] // 2 * 5  # Делит нацело на 2 и умнажает на 5
    print(listnums[i], end=' ')   # Выводим элементы В ОДНУ СТРОКУ