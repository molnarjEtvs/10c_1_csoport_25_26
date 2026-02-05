import os
os.system("cls")

szoveg = input("add meg a szöveget: ")
szotar = {}
for karakter in szoveg:
    if karakter not in szotar:
        szotar[karakter] = 1
    else:
        szotar[karakter] += 1

for kulcs,ertek in szotar.items():
    print(f"{kulcs}: {ertek}db")