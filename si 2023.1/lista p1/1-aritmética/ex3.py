x1, y1 = float(input('insert the x-cordinate of P1: ')), float(input('insert the y-cordinate of P1: '))
x2, y2 = float(input('insert the x-cordinate of P2: ')), float(input('insert the y-cordinate of P2: '))
d = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (1/2)
print(f'The Euclidian distance between P1 and P2 is {d}')