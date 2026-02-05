import os
os.system("cls")

tanulok = []
while True:
    nev = input("Add meg a nevet:")
    if nev.upper() == "VÉGE":
        break
    jegy = int(input("Add meg a jegyet: "))
    tanulo = {}
    tanulo['nev'] = nev
    tanulo['jegy'] = jegy
    tanulok.append(tanulo)

keresettTanulo = input("Add meg a tanuló nevét: ")
talalat = False

for tanulo in tanulok:
    if tanulo['nev'] == keresettTanulo:
        talalat = tanulo

if tanulo == False:
    print("nincs találat")
else:
    print(f"{tanulo['nev']} {tanulo['jegy']}")