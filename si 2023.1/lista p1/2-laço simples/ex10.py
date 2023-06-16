n = int(input('input n: '))
s = 0
divisores = []
for i in range(1, n):
    if n % i == 0:
        divisores.append(i)
        s += i
if s == n:
    print(divisores)
    print(f'{n} é um número perfeito')
else:
    print(f'{n} não é um número perfeito')