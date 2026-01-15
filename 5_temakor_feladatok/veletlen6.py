import os, random

szamTipus = input("Add meg hogy L/E: ")

if szamTipus == "L":
    szam = random.uniform(8,88)
elif szamTipus == "E":
    szam = random.randint(8,88)
else:
    szam = "Nem tudom értelmezni"

print(szam)