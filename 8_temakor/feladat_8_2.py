import os
os.system("cls")

def utikoltseg_szamolas(tavolsag:int,fogyasztas:float,benzin_ar:float,utasok:int = 1):
    fogyott_uzemanyag = (tavolsag/100) * fogyasztas
    teljes_utiktsg = fogyott_uzemanyag * benzin_ar
    egyforeJutoKtsg = teljes_utiktsg/utasok
    return egyforeJutoKtsg

egyeduli = utikoltseg_szamolas(500,6,600)
print(f"egydüli költség: {egyeduli} Ft")

telekocsi = utikoltseg_szamolas(200,8,610,4)
print(f"Telekocsival: {telekocsi} Ft")