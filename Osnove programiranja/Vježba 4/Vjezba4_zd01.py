#Anđela Vanesa Tuta, 16.11.2017
#Vjezba 4, zadatak 1

niz = input('Unesite niz znakova: ')

# a)
print('a)Duljina niza je ', len(niz))

#b)
print('b)Najveći element niza je ', max(niz))

#c)
print('c)Najmanji element  niza je ', min(niz))

#d)
print('d)Drugi znak  niza je ', niz[1])

#e)
print('e)Zadnji znak niza je '+niz[-1])

#f)
print('f)'+(niz+'.')*2+niz)

#g)
if len(niz)>=2:
  print('g)'+niz[1:-1])
else:
    print('g)')

#h)
print('h) Obrnuti redoslijed: '+niz[::-1])


#i)
print('i) Obrnuti redoslijed: '+niz[::2])

#j)
if 'a' in niz:
    print('j)Slovo a se pojavljuje na poziciji '+str(niz.index('a')+1))
else:
    print('Slovo a nije u zadanom nizu.')

