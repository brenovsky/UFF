n = int(input('input a number: '))
a = 0
b = 1
for i in range(n):
    b = b + a
    a = b - a
print(a)
