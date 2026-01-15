import os
os.system("cls")

szo = input("Add meg szót: ")
hossz = int(input("Add meg a hosszt: "))
karakter = input("Add meg a karaktert: ")
kozepre = szo.center(hossz,karakter)
print(kozepre)