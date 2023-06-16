n = int(input('input n: '))
sequence = []
i = 1
while n >= i:
    quadrado = False
    k = 1
    while i >= k:
        if i / k == k:
            quadrado = True
            sequence.append(i)
        k += 1
    i += 1
print(sequence)