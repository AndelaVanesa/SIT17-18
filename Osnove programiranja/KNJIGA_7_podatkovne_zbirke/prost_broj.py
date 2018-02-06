def prosto(x):  # definisanje funkcije
    if (x == 1):  # 1 nije prost broj
        return False  # povratak za 1 - nije prost broj
    for i in range(2, x):  # za sve od 2 do izabrano broja
        if (x % i == 0):  # djeljiv sa brojem i
            return False  # broj je djeljiv i nije prost
    return True  # nije djeljiv - nasao je prost broj


for p in range(1, 10000):  # brojevi iz opsega
    if prosto(p):  # poziv funkcije i provjera indikatora prost broj
        print(p)  # ispis broja
