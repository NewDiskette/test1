a, b, c = int(input()),int(input()),int(input())
m = [a, b, c]
m = sorted(m)
print('YES' if m[2] < m[1] + m[0] else 'NO')