girls = int(input('Введите количесвто девочек:'))   # Считывает количество девочек
apple = []  # Список
for i in range(1, girls + 1):
    apple.append(int(input()) - i)  # Отнимаем количество яблок от порядкового номера
for i in range(girls):
    print(apple[i])