a = int(input('input a: '))
b = int(input('input b: '))
A = []
B = []

for i in range(1, a + 1):
    if a % i == 0:
        A.append(i)

for i in range(1, b + 1):
    if b % i == 0:
        B.append(i)

for i in range(1, len(B)):
    if B[i] in A:
        print(f'{a} e {b} não são coprimos')
        break
    
else:
    print(f'{a} e {b} são coprimos')