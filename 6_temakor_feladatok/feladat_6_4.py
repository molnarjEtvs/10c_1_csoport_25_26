import os
os.system("cls")


csunyak = ["fasz","buzi","kurva"]
szepek = ["pénisz","homosexuális","prostituált"]

mondat = input("Adj meg egy mondatot: ")
for index in range(len(csunyak)):
    mondat = mondat.replace(csunyak[index],szepek[index])
print(mondat)