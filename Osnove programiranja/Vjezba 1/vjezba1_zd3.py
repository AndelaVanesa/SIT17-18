#Anđela Vanesa Tuta, 1.11.2017.
#vježba_1, zadatak 3

duljina_cm= 149
#zadana duljina u centimetrima
duljina_ft= duljina_cm//30.48
#izračun duljine u stopama
duljina_ostatak= duljina_ft%30.48
#ostatak pri pretvorbi
duljina_in= duljina_ostatak*0.393701
#izračun duljine ostatka

print('Duljina od',duljina_cm,'cm, odgovara duljini od',duljina_ft,'stopa i',str(round(duljina_in,2)),'inča.')