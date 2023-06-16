n = int(input('n coordinates: '))
a = []
b = []
p = 0
for i in range(n):
    a.append(int(input('input a-coordinates: ')))
for i in range(n):
    b.append(int(input('input b-coordinates: ')))
for i in range(n):
    p += a[i] * b[i]
print(p)