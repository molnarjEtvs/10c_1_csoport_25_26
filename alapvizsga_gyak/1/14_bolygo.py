import os
os.system("cls")

def bolygorogzites():
    bolygok=[]
    while True :
        bolygo=input("Add meg a bolygó nevét: ").capitalize()
        if not bolygo :
            break
        bolygok.append(bolygo)
    return bolygok
def bolygoelemzes(bolygok:list):
    db = len(bolygok)
    print(f"{db} bolygo kerult rozitesre ")
    ndb=0
    for elem in bolygok:
        if len(elem) == 4:
            ndb+=1
    sz="_$_".join(bolygok)
    print(f"4 betűsek száma:{ndb}db.")
    print(f"rögzített bolygók:{sz}")
b=bolygorogzites()
bolygoelemzes(b)
        
    