palavra = 'subinoonibus'
lista = []
palindromo = True
for i in range(len(palavra)):
    lista.append(palavra[i])
reverso = list(reversed(lista))
if lista != reverso:
    palindromo = False
print(palindromo)