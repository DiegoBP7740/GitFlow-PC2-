from ursina import *
from Alex import *
from Steve import Steve, Steve_default
from color_dict import *
from Alex import *

def menu2(character):
  

    print("Choose your preference: ")
    print("[1] Defined Colors")
    print("[2] RGB Colors")
    print("[3] Default Skin")
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
        
        print("Skin")
        
        s =int(input("Skin Color: "))

        skin = colors_dict[s]

        print("")
        print("Mouth")
        
        m = int(input("Mouth Color: "))

        mouth = colors_dict[m]

        print("")
        print("Eyes")

        e = int(input("Eyes color_dict: "))

        eyes = colors_dict[e]

        print("")
        print("Hair")

        h = int(input("Hair Color: "))
        
        hair = colors_dict[h]    

        #Character
        if character == "Alex":
            character_funtion = Alex(skin,mouth,eyes,hair)            
            print(character_funtion)
        


    elif option2 == 2:

        #RGB Colors

        print("RGB Colors Selected!")
        print("")
        print("Skin")
        r = int(input("R: "))
        g = int(input("G: "))
        b = int(input("B: "))

        skin = rgb(r,g,b)

        print("")
        print("Mouth")
        r = int(input("R: "))
        g = int(input("G: "))
        b = int(input("B: "))

        mouth = rgb(r,g,b)

        print("")
        print("Eyes")
        r = int(input("R: "))
        g = int(input("G: "))
        b = int(input("B: "))

        eyes = rgb(r,g,b)

        print("")
        print("Hair")
        r = int(input("R: "))
        g = int(input("G: "))
        b = int(input("B: "))

        hair = rgb(r,g,b)

        #Character
        if character == "Alex":
            character_funtion = Alex(skin,mouth,eyes,hair)            
            print(character_funtion)
        
        if character == "Steve":
            character_funtion = Steve(skin,mouth,eyes,hair)
            print(character_funtion)

    elif option2 == 3:
        if character == "Alex":
            print(Alex_default())
    
    elif option2 == 3:
        if character == "Steve":
            print(Steve_default())

        


