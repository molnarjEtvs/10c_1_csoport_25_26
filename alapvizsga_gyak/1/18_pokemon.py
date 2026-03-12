import os,random
os.system("cls")

class Pokemon:
    def __init__(self,dex:int,nev:str,ero:float):
        self.dex=dex
        self.nev=nev
        self.ero=ero
    def beallitas(self):
        self.ugrasi_magassag = self.ero * 3 * 0.885

    def kepessegvalasztas(self):
        kepessegek=["párolgás","tűzhányás","lövés","gurulás"]
        self.kepesseg = random.choice(kepessegek)

    def csoportositas(self,kor:int):
        if kor >= 15:
            self.csoport = "idős"
        else:
            self.csoport = "fiatal"

pokemonok = []
with open("pokemonLista.txt","r",encoding= "utf-8") as p:
    for sor in p:
        adatok = sor.strip().split(",")
        pokemon1 = Pokemon(int(adatok[0]),adatok[1],float(adatok[2]))
        pokemon1.beallitas()
        pokemon1.kepessegvalasztas()
        pokemon1.csoportositas(random.randint(1,50))
        pokemonok.append(pokemon1)

with open("pokeAdatok.txt", "w", encoding="utf-8") as k:
    for pokemon in  pokemonok:
        k.write(f"dex:{pokemon.dex}\n")
        k.write(f"nev:{pokemon.nev}\n")
        k.write(f"erő:{pokemon.ero}kp/ugrasimagassag{pokemon.ugrasi_magassag}m\n")   
        k.write(f"képpeség/csoport:{pokemon.kepesseg}/{pokemon.csoport}\n")
        k.write(f"*"*20)
        k.write("\n")