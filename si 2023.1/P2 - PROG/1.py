def primo(x):
    if x > 2:
        for i in range(2, x):
            if x % i == 0:
                return False
            return True
    elif x == 1:
        return False
    elif x == 2:
        return True
    
n = int(input())

soma = 0

for i in range(2, n + 1):
    if primo(i) == True:
        soma += i

print(soma) #na prova eu escrevi print(i) :(