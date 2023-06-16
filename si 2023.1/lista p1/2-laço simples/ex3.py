n = int(input('input n: '))
maior_antigo = int(input('input a number: '))
i = 1
while n > i:
    maior_novo = int(input('input a number: '))
    if maior_novo > maior_antigo:
        maior_antigo = maior_novo
    i += 1
print(f'O maior número é {maior_antigo}')