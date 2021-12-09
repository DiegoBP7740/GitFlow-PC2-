from ursina import *
from Blaze import *
from color_dict import *
from Magma import *
from Blaze import *
from Enderman import *
from Cow import *
from Sheep import *
from Zombie import *
from Creeper import *
from Squid import *

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

        elif character == "Magma":
            character_funtion = Magma(primary_color,secondary_color)
            print(character)
        
        elif character == "Enderman":
            character_funtion = Enderman(primary_color,secondary_color)
            print(character)

        elif character == "Cow":
            character_funtion = Cow(primary_color,secondary_color)
            print(character)
        
        elif character == "Sheep":
            character_funtion = Sheep(primary_color,secondary_color)
            print(character)
        
        elif character == "Zombie":
            character_funtion = Zombie(primary_color,secondary_color)
            print(character)
        
        elif character == "Creeper":
            character_funtion = Creeper(primary_color,secondary_color)
            print(character)

        elif character == "Squid":
            character_funtion = Squid(primary_color,secondary_color)
            print(character)
            
                            
    elif option2 == 2:

        if character == "Blaze":
            print(Blaze_default())

        elif character == "Magma":
            print(Magma_default())
            
        elif character == "Enderman":
            print(Enderman_default())

        elif character == "Cow":
            print(Cow_default())
        
        elif character == "Sheep":
            print(Sheep_default())
        
        elif character == "Zombie":
            print(Zombie_default())
        
        elif character == "Creeper":
            print(Creeper_default())
        
        elif character == "Squid":
            print(Squid_default())
                   
