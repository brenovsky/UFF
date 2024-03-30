n = int(input('input n: '))
menor_antigo = int(input('input a number: '))
i = 1
while n > i:
    menor_novo = int(input('input a number: '))
    if menor_novo < menor_antigo:
        menor_antigo = menor_novo
    i += 1
print(f'O menor número é {menor_antigo}')     