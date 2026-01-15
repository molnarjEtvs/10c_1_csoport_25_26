import os,random
os.system("cls")

fszam = int(input("Add meg a számot 10-1000: "))
gszam = random.randint(10,1000)
print(f"generált: {gszam}, bekért: {fszam}")

if gszam>fszam:
    print("A generált szám nagyobb")
elif gszam<fszam:
    print("A bekért szám nagyobb")
else:
    print("egyenlő a két szám")