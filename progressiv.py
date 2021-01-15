# Арифметическая прогрессия
a1, a2, a3 = int(input()), int(input()), int(input())
d = a2 - a1
if a3 == a2 + d:
    print('YES')
else:
    print('NO')