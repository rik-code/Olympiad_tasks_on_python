vozmojnost = 0
stolb = int(input())
stroka = int(input())
# Конь идёт вправо
if stolb + 2 <= 8:
    if stroka + 1 <= 8:  # и вверх
        vozmojnost += 1
    if stroka - 1 > 0:   # и вниз
        vozmojnost += 1
# Конь ходит влево
if stolb - 2 > 0:
    if stroka + 1 <= 8:  # и вверх
        vozmojnost += 1
    if stroka - 1 > 0:   # и вниз
        vozmojnost += 1
# Конь ходит вверх
if stroka + 2 <= 8:
    if stolb + 1 <= 8:
        vozmojnost += 1     # и вправо
    if stolb - 1 > 0:
        vozmojnost += 1     # и влево
# Конь ходит вниз
if stroka - 2 > 0:
    if stolb + 1 <= 8:
        vozmojnost += 1  # и вправо
    if stolb - 1 > 0:
        vozmojnost += 1  # и влево


print(vozmojnost)