#Anđela Vanesa Tuta,2.11.2017.
#vježba 2, zadatak 5

sekunde_input = int(input('Molimo unesite vrijeme u sekundama: '))

#funkcija divmod računa cjelobrojni kvocijent i ostatak pri dijeljenju
minute, sekunde = divmod(sekunde_input, 60)
#sekunde_input//60, sekunde_input%60
sati, minute = divmod(minute, 60)
#minute//60, minute%60
dani, sati = divmod(sati, 24)
#sati//24, sati%24
print(sekunde_input, 'sekundi je ',dani,'dana, ',sati,'sati,', minute,'minuta i', sekunde,'sekundi.')
#print('{0} dana, {1} sati, {2} minuta i {3} sekundi' .format(dani, sati, minute, sekunde))
#.format-navod za više argumenata
#brojevi u listi uvijek su definirani
#numeracija kreće od nule

print('{0} dana, {1} sati, {2} minuta i {3} sekundi' .format(dani, sati, minute, sekunde))

#:f-> ispis decimalnog broja, :d-> ispis cijelog broja :s->ispis stringa---->stavlja se iza umetnutog elementa liste, unutar {}
