def fatorial(x):
    P = 1
    for i in range(2, x + 1):
        P *= i
    return P

def combinar(x, y):
    return fatorial(x) // ((fatorial(x - y)) * fatorial(y))

n = int(input('input n: '))
k = int(input('input k: '))

print(f'A combinação de {n} por {k} é {combinar(n, k)}')