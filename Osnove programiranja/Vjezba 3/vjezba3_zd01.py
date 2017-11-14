#Andela Vanesa Tuta, 10.11.2017
#Vjezba 3, zadatak


while True:
  #varijable x i y predstavljaju par koordinata
  x = float(input('Unesite koordinatu x: '))
  y = float(input('Unesite koordinatu y: '))



  if x == 0 and y == 0:
    print('Točka ({}, {}) se nalazi u ishodištu koordinatnog sustava.'.format(x, y))
  elif x == 0:
    print('Točka ({}, {}) leži na y osi.'.format(x, y))
  elif y == 0:
    print('Točka ({}, {}) leži na x osi.'.format(x, y))
  elif x and y > 0:
    print('Točka {},{} nalazi se u I. kvadrantu'.format(x,y))
  elif x < 0 and y > 0:
    print('Točka {},{} nalazi se u II. kvadrantu'.format(x,y))
  elif x < 0 and y < 0:
    print('Točka {},{} nalazi se u III. kvadrantu'.format(x,y))
  elif x > 0 and y < 0:
    print('Točka {},{} nalazi se u IV. kvadrantu.'.format(x,y))

  nastavak = input("Želite nastaviti (d/n)? ")

  if nastavak == 'n':
      break