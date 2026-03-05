import os
os.system("cls")

class Pokemon:
    def __init__(self,dex:int,nev:str,ero:float):
        self.dex=dex
        self.nev=nev
        self.ero=ero
    def beallitas(self):
        self.ugrasi_magassag = self.ero * 3 * 0.885