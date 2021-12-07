from ursina import *
from menu2 import *

print("Skin Minecraft Creator")

name = input("Username: ")

print(f"Welcome {name} !!")
print("")
print("Choose your character ")
print("")
print("[1] Steve")
print("[2] Alex")
print("[3] Enderman")
print("[4] Creeper")
print("")
option = int(input("Send your option: "))

if option == 1:
    print(f"Opcion selected [Steve] ")
elif option ==2:
    print(f"Opcion selected [Alex] ")
    print("")
    menu2(Alex)
    

elif option == 3:
    print(f"Opcion selected [Enderman] ")
elif option == 4:
    print(f"Opcion selected [Creeper] ")


