import os
os.system("cls")

brutto = int(input("Add meg a bruttó fizetésed: "))
kor = int(input("Add meg hány éves vagy: "))
szja = brutto * 0.15
if kor<25:
    szja = 0
tb = brutto * 0.185
szocho = brutto * 0.13

netto = brutto - szja - tb
munktsg = brutto + szocho

print(f"A fizetésedből levont SZJA összege: {szja} Ft, TB összeg: {tb} Ft\nA nettó fizetésed: {netto} Ft\nA munkáltató ezt az összeget utalta el neked: {munktsg} Ft")