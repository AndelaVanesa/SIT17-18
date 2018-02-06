import random

n = int(input('Unesi broj:' ))
l1=[]
l2=[]
l3=[]
l4=[]
l5=[]
for i in range(5):
    l1.append(random.randint(0,10))
    l2.append(random.randint(0,10))
    l3.append(random.randint(0,10))
    l4.append(random.randint(0,10))
    l5.append(random.randint(0,10))

print(l1,l2,l3,l4,l5)

s=0
for i in range (len(l1)):
    s+=i

s1=0
for j in range (len(l2)):
    s1+=j

s2=0
for k in range (len(l3)):
    s2+=k

s3=0
for l in range (len(l4)):
    s3+=l

s4=0
for n in range (len(l5)):
    s4+=n

if s>s1 and s>s2 and s>s3 and s>s4:
    print("lista s najvecim zbr je",l1)

if s1 > s2 and s1 > s3 and s1 > s4:
     print("lista s najvecim zbr je", l2)

if s2 > s3 and s2 > s4:
     print("lista s najvecim zbr je", l3)

if s3>s4:
    print("lista s najvecim zbr je",l4)
else:
    print("lista s najvecim zbr je",l5)