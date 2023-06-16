k = int(input('input k: '))
m = 3
while k > 0:
    p = 2
    while m >= 2 ** p - 1:
        i = 2
        if 2 ** p - 1 == m:
            primo = True
            while m // 2 > i:
                if m % i == 0 and primo:
                    primo = False
                    break
                i += 1
            if primo == True:
                print(m)
                k -= 1
                break
        p += 1
    m += 1











#se é mersenne ou não dado m;
#m = int(input('input m: '))
#p = 2
#while m > p:
#    mersenne = False
#    if 2 ** p - 1 == m:
#        mersenne = True
#        break
#    p += 1
#if mersenne == True:
#    print(f'{m} é mersenne')
#else:
#    print(f'{m} não é mersenne')








#identificar se é mersenne ou não dado p;
#p = int(input('input p: '))
#mersenne = True
#m = 2 ** p - 1
#for i in range(2, m):
#    if m % i == 0:
#        mersenne = False
#if mersenne == True:
#    print(f'{m} é mersenne')
#else:
#    print(f'{m} não é mersenne')