import os
os.system("cls")

def fizetes_szamolas(oraszam:int,oraber:float,tulora_szorzo:float = 1.5):
    fizetes = 0
    if oraszam<=40:
        fizetes = oraszam * oraber
    else:
        alap = 40 * oraber
        tulora = (oraszam-40)*(oraber*tulora_szorzo)
        fizetes = alap+tulora
    return fizetes

normal_fizetes = fizetes_szamolas(35,2000)
print(f"{normal_fizetes} Ft")

tulora_alap = fizetes_szamolas(45,2000)
print(f"{tulora_alap} Ft")

tulora_egyedi = fizetes_szamolas(42,2000,2.0)
print(f"{tulora_egyedi} Ft")