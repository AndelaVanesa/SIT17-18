#Anđela Vanesa Tuta , 1.11.2017.
#vjezba_1, zadatak_5

sekunde=23563

dani=sekunde//(24*60*60)
sekunde_ostatak=sekunde%(24*60*60)

sati=sekunde_ostatak//(60*60)

sekunde_ostatak%=60**2

minute=sekunde_ostatak//60
sekunde_ostatak%=60

print(sekunde, 'sekunde jednako je',dani,'dana,',sati,'sati',minute,'minute',sekunde_ostatak,'sekunde')
