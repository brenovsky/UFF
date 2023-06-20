def inverter(x):
    nova = []
    for i in range(len(x)):
        if x[i] not in nova:
            nova.append(x[i])
    nova_invertida = []
    for i in range(len(nova) - 1, -1, -1):
        nova_invertida.append(nova[i])
    return nova_invertida

lista = [1, 2, 7, 2, 2, 2, 5, 6, 6, 6, 1]
print(inverter(lista))

#------------------------------------------------------------#

#código que fiz na prova (errei :D)
#coloquei o len da lista mesmo elementos sendo deletada :(
#mas a intenção foi boa!!

#def inverter(x):
#    for i in range(len(x)):
#        for j in range(len(x)):
#            if x[i] == x[j] and i != j:
#                del x[j]
#    nova = list(reversed(x))
#    return nova

#lista = [1, 1, 1, 2]
#print(inverter(lista))