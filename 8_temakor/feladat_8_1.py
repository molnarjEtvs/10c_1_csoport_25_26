import os, fuggvenyeim
os.system("cls")

orasz = int(input("Add meg mennyi órát dolgoztál: "))
normal_fizetes = fuggvenyeim.fizetes_szamolas(orasz,2000)
print(f"{normal_fizetes} Ft")

tulora_alap = fuggvenyeim.fizetes_szamolas(45,2000)
print(f"{tulora_alap} Ft")

tulora_egyedi = fuggvenyeim.fizetes_szamolas(42,2000,2.0)
print(f"{tulora_egyedi} Ft")