m = int(input())  #  месяц
if m == 2:
    print(28)
elif m in [1, 3, 5, 7, 8, 10, 12]:
    print(31)
else:
    print(30)