n = int(input('insert $: '))
notas = [200, 100, 50, 20, 10, 5, 2, 1]
k = 0
for i in range(len(notas)):
    x = 0
    while n >= notas[i]:
        n -= notas[i]
        x += 1
    print(f'{x} notas de R${notas[i]}')
    k += x
print(f'são utiizadas {k} notas')