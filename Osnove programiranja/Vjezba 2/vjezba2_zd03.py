#Anđela Vanesa Tuta,2.11.2017.
#Vježba 2, zadatak 3

duljina_cm = int(input('Molim, unesite duljinu u centimetrima: '))
duljina_ft = duljina_cm//30.48
duljina_ostatak = duljina_ft%30.48
duljina_inch= duljina_ostatak*0.39


print('Duljina od {} cm odgovara duljini od {} stopa i {:0.2f} inča.' .format(duljina_cm,duljina_ft,duljina_inch))





