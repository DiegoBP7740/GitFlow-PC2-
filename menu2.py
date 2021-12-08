from ursina import *
from Alex import Alex
from color_dict import *

def menu2(character):
  

    print("Choose your preference: ")
    print("[1] Defined Colors")
    print("[2] RGB Colors")
    print("")
    option2 = int(input("Send your preference: "))

    if option2 == 1:

        #Defined Colors

        print("Definided Colors Selected!")
        print("")
        print("Our Colors")
        print("")
        print(f"[1] White       [7] Brown")
        print(f"[2] Black       [8] Gold")
        print(f"[3] Red         [9] Dark Gray")
        print(f"[4] Orange      [10] Light Gray")
        print(f"[5] Yellow      [11] Magenta")
        print(f"[6] Green       [12] Pink")
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
        character_funtion = Alex(skin,mouth,eyes,hair)
        print(character_funtion)

        


    if option2 == 2:

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

        #Funtion
        
        if character == "Alex":
          character_funtion = Alex(skin,mouth,eyes,hair)
          print(character_funtion)
          
        elif charecter == "Steve":
          character_funtion = Alex(skin,mouth,eyes,hair)
          print(character_funtion)
          

print(menu2(Alex))
