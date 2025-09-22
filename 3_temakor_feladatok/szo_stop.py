import os
os.system("cls")

#1 lehetőség:
szo = ""
while szo != "STOP":
    szo = input("Adj meg egy szót: ")

print("A program futás vége")


#2. lehetőség
while True:
    szo = input("Adj meg egy szót: ")
    if szo == "STOP":
        break
print("A program futás vége")