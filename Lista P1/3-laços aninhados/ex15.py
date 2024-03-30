n = int(input('input n: '))
k = int(input('input k: '))
lista = list(map(int, input().split()))
for x in range(1, k + 1):
    contador = 0
    for i in range(len(lista)):
        if x == lista[i]:
            contador += 1
    print(f'{x}:', '#' * contador)