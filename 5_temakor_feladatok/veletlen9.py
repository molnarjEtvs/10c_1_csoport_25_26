import os,random
os.system("cls")

tanulok = []
sorszam = 1
while True:
    nev = input(f"Add meg a(z) {sorszam}. tanuló nevét: ")
    sorszam += 1
    if not nev:
        break
    tanulok.append(nev)

felelok = random.sample(tanulok,2)
print(f"Az első felelő: {felelok[0]}")
print(f"Az másdik felelő: {felelok[1]}")
