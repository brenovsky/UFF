def primo(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

def palindromo(x):
    if x > 10:
        reverso = []
        while x > 0:
            reverso.append(x % 10)
            x //= 10
        if reverso == list(reversed(reverso)):
            return True
        return False
    return False

n = int(input())
k = 11
while n > 0:
    if primo(k) == True and palindromo(k) == True:
        print(k)
        n -= 1
    k += 1