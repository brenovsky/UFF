n = int(input('input n: '))
lista = []
for i in range(n):
    P = float(input('input P: '))
    G = int(input('input G: '))
    valor = (P * 1000) / G
    lista.append(valor)
print(min(lista))