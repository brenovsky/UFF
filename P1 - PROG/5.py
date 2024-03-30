n = int(input('input n: '))
p = 0
a = []
b = []
for i in range(n):
    a.append(int(input('input a coordinates: ')))
for i in range(n):
    b.append(int(input('input b coordinates: ')))
for i in range(n):
    p += a[i] * b[i]
print(p)