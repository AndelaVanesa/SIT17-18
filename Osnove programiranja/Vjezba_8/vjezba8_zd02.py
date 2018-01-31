#Anđela Vanesa Tuta, 21.12.2017.
#Vjezba 8, zadatak 1

def palindrom (s):

    slova = list(s)
    palindrom = True

    for i in slova:
     if i == slova[-1]:
        slova.pop(-1)
     else:
        palindrom = False
        break

    return palindrom
