import os
os.system("cls")

szam = int(input("Adj meg egy számot: "))

if szam%3==0:
    print(f"A {szam} osztható 3-al")
else:
    print(f"A {szam} nem osztható 3-al")