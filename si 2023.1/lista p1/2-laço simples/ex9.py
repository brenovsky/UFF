n = int(input('insert n: '))
quadrado = False
i = 1
while n >= i and quadrado == False:
    if n / i == i:
        quadrado = True
    i += 1
if quadrado == False:
    print(f'{n} não é um quadrado perfeito')
else:
    print(f'{n} é um quadrado perfeito')
    print(f'{i - 1} * {i - 1} = {n}')