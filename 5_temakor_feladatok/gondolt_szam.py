import os,random
os.system("cls")

gondoltSzam = random.randint(1,1000)

sorszam = 1
while True:
    tipp = int(input(f"Add meg a(z){sorszam}. tipped: "))
    sorszam += 1
    if tipp==gondoltSzam:
        print("Gratulálok")
        break
    elif tipp>gondoltSzam:
        print("A tipp nagyobb")
    else:
        print("A tipp kisebb")