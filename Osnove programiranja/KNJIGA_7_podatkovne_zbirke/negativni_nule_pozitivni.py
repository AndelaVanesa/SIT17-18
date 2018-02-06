
#26.1. Za deset učitanih brojeva ispisati koliko ima negativnih, nula i pozitivnih.
# 26011050
brneg = 0
brnul = 0
brpoz = 0
for i in range(1,11):
    x = int(input())
    if x < 0:
        brneg=brneg+ 1
    if x  == 0:
        brnul = brnul + 1
    if x > 0:
        brpoz = brpoz + 1
print("Učitano je", brneg, "negativnih")
print("Učitano je", brnul, "nula")
print("Učitano je", brpoz, "pozitivnih")