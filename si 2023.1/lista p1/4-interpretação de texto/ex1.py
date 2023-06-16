cor_1 = int(input('cor 1: '))
cores = [cor_1]
cores_iguais = 0
for i in range(2, 5):
    cor = int(input(f'cor {i}: '))
    if cor in cores:
        cores_iguais += 1
    cores.append(cor)
print(f'Precisa-se de, no mínimo, {cores_iguais} ferradura(s)')