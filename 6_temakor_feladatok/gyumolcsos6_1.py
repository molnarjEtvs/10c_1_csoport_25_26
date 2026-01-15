import os
os.system("cls")

gyumolcsok = []
while True:
    gyumolcs = input("Add meg a gyümölcs nevét: ").capitalize()
    if not gyumolcs:
        break
    gyumolcsok.append(gyumolcs)

print(gyumolcsok)