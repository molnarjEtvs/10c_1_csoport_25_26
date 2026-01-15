import os,random
os.system("cls")

nyeroSzamok = []

while len(nyeroSzamok)<5:
    vszam = random.randint(1,90)
    if vszam not in nyeroSzamok:
        nyeroSzamok.append(vszam)

nyeroSzamok.sort()

talalatok = 0
tippek = []
while len(tippek)<5:
    tipp = int(input("Add meg a tipped: "))
    if tipp>=1 and tipp<=90 and tipp not in tippek:
        tippek.append(tipp)
        if tipp in nyeroSzamok:
            talalatok += 1

tippek.sort()

print(nyeroSzamok)
print(tippek)
print(f"{talalatok} db")