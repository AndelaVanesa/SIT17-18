

niz = '0123456789'

for i in niz:
    for j in niz:
        if i==j: continue
        print((i+j).center(3), end = ' ')
    print()