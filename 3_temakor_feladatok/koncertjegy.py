import os
os.system("cls")

szektor_ar = 6500
paholy_ar = 9800
diak_kedvezmeny = 0.75
fizetendo = 0
hely = input("Hova szeretnél jegyet? Páholy (P), Szektor (S):")
db = int(input("Mennyi jegyet szeretnél? (db): "))
diak_e = input("Diák vagy? Igen (i), Nem (n): ")

if hely == "P":
    fizetendo = db*paholy_ar
elif hely == "S":
    fizetendo = db * szektor_ar
else:
    print("Ilyen jegytípus nincs!")

if diak_e == "i":
    fizetendo = fizetendo * 0.75

print(f"Fizetendő összeg: {fizetendo} Ft")