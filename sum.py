a, b, c = (int(input()) for _ in range(3))
if a < 0:
    a = 0
if b < 0:
    b = 0
if c < 0:
    c = 0 
print(a + b + c) 

print('next')

s = 0
for i in range(3):
  a = int(input())
  if a > 0:
    s += a
print(s)

print('next')

print(sum([i for i in [int(input()) for _ in 'abc'] if i > 0]))