n = int(input())

antiga = [1, 0]

print(' '.join(map(str, antiga[:1])))

for i in range(n - 1):
    auxiliar = [1]
    for j in range(n - 1):
        auxiliar.append(antiga[j] + antiga[j + 1])
        if auxiliar[-1] == 1:
            auxiliar.append(0)
            break
    nova = auxiliar[:len(auxiliar) - 1]
    print(' '. join(map(str, nova)))
    antiga = auxiliar