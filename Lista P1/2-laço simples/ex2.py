crescente = True
numero_novo = 1
numero_antigo = 0
while numero_novo != 0:
    numero_novo = int(input('insira o numero: '))
    if numero_novo != 0:
        if numero_novo < numero_antigo:
            crescente = False
        numero_antigo = numero_novo
if crescente == True:
    print('Estão em ordem crescente')
else:
    print('Não estão em ordem crescente')