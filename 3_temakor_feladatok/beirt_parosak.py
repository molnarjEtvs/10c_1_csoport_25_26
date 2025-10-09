import os
os.system("cls")

parosDb = 0
szam = 1
while szam != 0:
    szam = int(input("Adj meg egy számot: "))
    if szam%2==0:
        parosDb += 1
print(f"A páros darabszám: {parosDb}")