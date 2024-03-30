n = int(input('input n: '))
p = 1
if n >= 0:
    for i in range(2, n + 1):
        p = p*i
    print(f'{n}! = {p}')
else: 
    print('Interval error.')
    