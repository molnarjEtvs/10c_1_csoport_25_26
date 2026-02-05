import os
os.system("cls")

telfonszamok = []
while True:
    nev = input("Add meg a nevet: ")
    if nev.upper() == "VÉGE":
        break
    teleszam = input("Add meg a telfonszámot: ")
    ugyfel = {}
    ugyfel['nev'] = nev
    ugyfel['telefonszam'] = teleszam
    telfonszamok.append(ugyfel)

keresettNev = input("Add meg kit keresel: ")
talalat = False
for ember in telfonszamok:
    if ember['nev'] == keresettNev:
        talalat = ember

if talalat == False:
    print("Nincs találat")
else:
    print(f"{talalat['nev']} teleszáma: {talalat['telefonszam']}")


lista = ["alma","körte"]

lista[1] = "szilva"