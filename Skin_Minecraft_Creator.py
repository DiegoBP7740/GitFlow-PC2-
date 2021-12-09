from ursina import *
from menu2 import *
from menu2 import *
from menu3 import *

print("Skin Minecraft Creator")

name = input("Username: ")
print("")
print(f"Welcome {name} !!")
print("")
print("Choose your character ")
print("")
print(f"[1] Steve      [7] Pig")
print(f"[2] Alex       [8] Magma")
print(f"[3] Creeper    [9] Blaze")
print(f"[4] Zombie     [10] Sheep")
print(f"[5] Skeleton   [11] Spider")
print(f"[6] Cow        [12] Enderman") 
print(f"               [13] Squid")       

print("")
option = int(input("Send your option: "))
print("")

if option == 1:
    print(f"Opcion selected [Steve] ")
    menu2("Steve")

elif option == 2:
    print(f"Opcion selected [Alex] ")
    print("")
    print(menu2("Alex"))

elif option == 3:
    print(f"Opcion selected [Creeper] ")
    print("")
    print(menu3("Creeper"))

elif option == 4:
    print(f"Opcion selected [Zombie] ")
    print("")
    print(menu3("Zombie"))

elif option == 5:
    print(f"Opcion selected [Skeleton] ")
    print("")
    print(menu3("Skeleton"))

elif option == 6:
    print(f"Opcion selected [Cow] ")
    print("")
    print(menu3("Cow"))

elif option == 7:
    print(f"Opcion selected [Pig] ")
    print("")
    print(menu3("Pig"))

elif option == 8:
    print(f"Opcion selected [Magma] ")
    print("")
    print(menu3("Magma"))

elif option == 9:
    print(f"Opcion selected [Blaze] ")
    print("")
    print(menu3("Blaze"))

elif option == 10:
    print(f"Opcion selected [Sheep] ")
    print("")
    print(menu3("Sheep"))

elif option == 11:
    print(f"Opcion selected [Spider] ")
    print("")
    print(menu3("Spider"))

elif option == 12:
    print(f"Opcion selected [Enderman] ")
    print("")
    print(menu3("Enderman"))

elif option == 13:
    print(f"Opcion selected [Squid] ")
    print("")
    print(menu3("Squid"))




    
    





