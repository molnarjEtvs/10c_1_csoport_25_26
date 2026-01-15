import os, random

veletlenSzamok = []
db = int(input("Hány db számot szerenél: "))

for _ in range(db):
    vszam = random.randint(100,1000)
    veletlenSzamok.append(vszam)

print(veletlenSzamok)