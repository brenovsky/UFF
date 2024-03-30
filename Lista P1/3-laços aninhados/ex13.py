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

print(palindromo(int(input())))