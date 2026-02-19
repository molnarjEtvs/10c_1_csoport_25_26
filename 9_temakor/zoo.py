import os
os.system("cls")


allatok = []
with open("allatok.txt","r",encoding="utf-8") as f:
    for sor in f:
        adat = sor.strip().split(";")
        allat = {}
        allat['nev'] = adat[0]
        allat['faj'] = adat[1]
        allat['suly'] = float(adat[2])
        allat['kor'] = int(adat[3])
        allatok.append(allat)

db = len(allatok)
print(f'Az állatok száma: {db} db')

db_oroszlan = 0
for allat in allatok:
    if allat['faj'] == "Oroszlán":
        db_oroszlan += 1

print(f"Oroszlánok száma: {db_oroszlan} db")

legnehezebbAllat = allatok[0]

for allat in allatok:
    if allat['suly']>legnehezebbAllat['suly']:
        legnehezebbAllat = allat

print(f"A legnehezebb állat: {legnehezebbAllat['nev']}")

with open('nyugdijasok.txt',"w",encoding="utf-8") as f:
    for allat in allatok:
        if allat['kor']>15:
            f.write(f"{allat['nev']};{allat['faj']}\n")
