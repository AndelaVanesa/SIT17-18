
niz = str(input('Unesite niz znakova: '))
velika_slova = 0
mala_slova = 0
znamenke = 0
ostalo = 0


for i in niz:
    if(i.islower()):
        mala_slova += 1
    if(i.isupper()):
        velika_slova += 1
    if(i.isdigit()):
        znamenke += 1
    ostalo = len(niz)- (velika_slova + mala_slova + znamenke)


print('Unos sadzži {} velikih slova, {} malih slova, {} brojeva i {} ostalih znakova.'.format(velika_slova,mala_slova,znamenke,ostalo))
#Parni 324, neparni 12345.