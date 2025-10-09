import os
os.system("cls")

osszeg = 0
szam = 1
while szam != 0:
    szam = int(input("Add meg a számot: "))
    osszeg += szam
print(f"Összeg: {osszeg}")

