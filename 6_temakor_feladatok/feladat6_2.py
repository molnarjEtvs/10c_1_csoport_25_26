import os
os.system("cls")

mondat = input("Adj meg egy mondatot: ")
szo = input("Add meg a szót: ")

if mondat.startswith(szo) == True:
    print("Kezdődik")
elif mondat.endswith(szo) == True:
    print("Végződik")
else:
    print("egyik sem")