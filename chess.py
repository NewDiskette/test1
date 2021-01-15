x1, y1 = int(input()), int(input()) 
x2, y2 = int(input()), int(input()) 
x = x1 - x2
y = y1 - y2
if x == 0 and y == 0:
    print('NO')
elif -1 <= x <= 1 and -1 <= y <= 1:
    print('YES')
else:
    print('NO')