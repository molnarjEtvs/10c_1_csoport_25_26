import os, random

veletlenSzamok = []
db = int(input("Hány db számot szerenél: "))
kezd = int(input("Add meg a kezdőértéket: "))
veg = int(input("Add meg a végértéket: "))

for _ in range(db):
    vszam = random.randint(kezd,veg)
    veletlenSzamok.append(vszam)

print(veletlenSzamok)