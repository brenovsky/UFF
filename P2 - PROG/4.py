fim = False

while fim == False:
    palavra = input()
    if palavra != 'FIM':
        lista = []
        for i in range(len(palavra)):
            lista.append(palavra[i])
        reverso = list(reversed(lista))
        if lista == reverso:
            print('é plaíndromo')
        else:
            print('não é palíndromo')
    else:
        fim = True