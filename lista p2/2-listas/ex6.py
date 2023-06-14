def soma(x):
    for a in range(x):
        for b in range(x):
            for c in range(x):
                lista = [a, b, c]
                if sum(lista) == x and a <= b and b <= c:
                    print(lista)

n = int(input('input n: '))

print(soma(n))