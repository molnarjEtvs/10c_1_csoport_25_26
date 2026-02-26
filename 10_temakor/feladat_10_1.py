import os
os.system("cls")

class Macska:

    def __init__(self,nev:str,suly:float,ehes:bool):
        self.nev = nev
        self.suly = suly
        self.ehes = ehes

    def eszik(self,eteleMennyiseg:float):
        if self.ehes == True:
            self.suly += eteleMennyiseg
            self.ehes = False
            return True
        else:
            return False
    
    def futkos(self):
        self.suly -= 0.1
        if self.ehes == False:
            self.ehes = True


    def jelenlegiErtekek(self):
        print(f"Név: {self.nev}")
        print(f"Súly: {self.suly} kg")
        if self.ehes == True:
            print("Éhes: IGEN")
        else:
            print("Éhes: NEM")


macska1 = Macska("Cirmi",3.5,True)
macska2 = Macska("Sanyika",4.8,False)

if macska1.eszik(0.4) == True:
    print(f"{macska1.nev} evett")
else:
    print(f"{macska1.nev} NEM evett")

if macska2.eszik(0.4) == True:
    print(f"{macska2.nev} evett")
else:
    print(f"{macska2.nev} NEM evett")

macska1.futkos()
macska2.futkos()

macska1.jelenlegiErtekek()
macska2.jelenlegiErtekek()