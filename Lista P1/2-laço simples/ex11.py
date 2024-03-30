n = int(input('input a number: '))
s = 0
c = 0
for i in range(1, n + 1):
    if n % i == 0:
        s += i
        c += 1
if s % c == 0:
    print(f'{n} é um número aritmético')
else:
    print(f'{n} não é um número aritmético')





#código antes
#n = int(input('input n: '))
#i = 1
#s = 0
#divisores = []
#for i in range(1, n + 1):
#    if n % i == 0:
#        divisores.append(i)
#        s += i
#if s % len(divisores) == 0:
#    print(f'{n} é um número aritmético')
#else:
#    print(f'{n} não é um número aritmético')