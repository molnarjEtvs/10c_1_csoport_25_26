import os,math
os.system("cls")

try:
    sugar=int(input("Add meg a sugarat: "))
    magassag=int(input("add meg a magasságot: "))
    pi=3.14
    V=sugar**2*pi*magassag/3
    a=math.sqrt(sugar**2 + magassag**2)
    A=sugar**2*pi+sugar*pi*a
    V=round(V,2)
    A=round(A,2)
    if A >= 10:
        print("A felszín legalább 10")
except:
    print("Hibás adatbevitel!")
