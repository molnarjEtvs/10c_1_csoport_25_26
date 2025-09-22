import os
os.system("cls")
 
szam = int(input("Adj meg egy pozitív egész számot: "))

for x in range(0,(szam+1)):
    if x%4 == 0:
        print(x)