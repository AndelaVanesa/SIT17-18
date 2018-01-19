
k = int(input('Unesi k: '))

i = 2
j = 0
while j < k:
    if i % 3 == 0 or i % 5 == 0:
        j += 1
        print(i, end='')
        i += 2
    else:
        i += 2