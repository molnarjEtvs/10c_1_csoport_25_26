import os
os.system("cls")

szam1 = int(input("Add meg a kezdő értéket: "))
szam2 = int(input("Add meg a végértéket: "))

for x in range(szam1,(szam2+1)):
    if x%2 == 0:
        print(x)