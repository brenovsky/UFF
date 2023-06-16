#código que fiz na prova (errei :D)
#coloquei o len da lista mesmo elementos sendo deletada :(
#mas a intenção foi boa!!

def inverter(x):
    for i in range(len(x)):
        for j in range(len(x)):
            if x[i] == x[j] and i != j:
                del x[j]
    nova = list(reversed(x))
    return nova

lista = [1, 1, 1, 2]
print(inverter(lista))