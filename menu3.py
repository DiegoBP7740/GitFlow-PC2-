from ursina import *
from Alex import *
from Blaze import Blaze, Blaze_default
from color_dict import *
from Magma import *

def menu3(character):
  

    print("Choose your preference: ")
    print("[1] Defined Colors")
    print("[2] Default Skin")
    print("")
    option2 = int(input("Send your preference: "))

    if option2 == 1:

        #Defined Colors

        print("Definided Colors Selected!")
        print("")
        print("Our Colors")
        print("")
        print(f"[1] White       [8] Brown")
        print(f"[2] Black       [9] Gold")
        print(f"[3] Red         [10] Dark Gray")
        print(f"[4] Orange      [11] Light Gray")
        print(f"[5] Yellow      [12] Magenta")
        print(f"[6] Green       [13] Pink")
        print(f"[7] Blue")
        print("")
        
        print("Primary Color")
        
        c1 =int(input("C1: "))

        primary_color = colors_dict[c1]

        print("")
        print("Secondary Color")

        c2 = int(input("C2: "))

        secondary_color = colors_dict[c2]
               
        #Character
        if character == "Blaze":
            character_funtion = Blaze(primary_color,secondary_color)          
            print(character_funtion)

        if character == "Magma":
            character_funtion = Magma(primary_color,secondary_color)
            print(character)

    elif option2 == 2:

        if character == "Blaze":
            print(Blaze_default())

        elif character == "Magma":
            print(Magma_default())

print(menu3("Magma"))