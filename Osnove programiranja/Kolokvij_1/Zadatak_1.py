

import math

a, b, c = 2, 4, 1

d = b ** 2 - 4 * a * c

if d<0:

    print("Jednadžba nema realnih rješenja pošto je D < 0:",round(d,2))
elif d==0:
    x1=(-b)/(2*a)
    print("Jednadžba ima jedno dvostruko rješenje pošto je D = 0:",round(x1,2))
elif d>0:
    x1=(-b+math.sqrt(d))/(2*a)
    x2=(-b-math.sqrt(d))/(2*a)
    print("Jednadžba ima dva rješenja pošto je D > 0:",round(d,2))
    print("Rješenje x1:",round(x1,2))
    print("Rješenje x2:",round(x2,2))