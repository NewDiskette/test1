num = [int(input()), int(input()), int(input()), int(input())]
num = sorted(num)
print(num[0])

print('next')

print(min(int(input()), int(input()), int(input()), int(input())))

print('next')

a, b, c, d = (int(input()) for _ in range(4)) 
print(min(a, b, c, d))

print('next')

print(min(int(input()) for i in range(4)))

