import os
os.system("cls")

valasz = input("Milyen napod van? (igen/nem): ")
if valasz == "igen":
    print("ez egy jó nap")
elif valasz == "nem":
    print("ez egy szörnyű nap")
else:
    print("nem tudom értelmezni")