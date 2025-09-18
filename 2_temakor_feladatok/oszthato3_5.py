import os
os.system("cls")

szam = int(input("Adj meg egy számot: "))

if szam%3==0 and szam%5==0:
    print("3-al és 5-el is osztható")
elif szam%3==0:
    print("csak 3-al osztható")
elif szam%5==0:
    print("Csak 5-el oszhtató")
else:
    print("Egyikkel sem osztható")