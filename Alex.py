from ursina import *

def Alex(skin,mouth,eyes,hair):
    app = Ursina()


    #Skin
    for x in range(8):
        a = Entity(model="cube",color = skin ,position = (x,1,0))

    for x in range(8):
        if x != 3 and x != 4:
            a = Entity(model="cube",color = skin ,position = (x,2,0))

    for x in range(8):
        a = Entity(model="cube",color = skin ,position = (x,3,0))

    for x in range(8):
        if x != 1 and x != 2 and x != 5 and x != 6:
            a = Entity(model="cube",color = skin ,position = (x,4,0))

    for x in range(3,7):
        a = Entity(model="cube",color = skin ,position = (x,5,0))

    for x in range(4,6):
        a = Entity(model="cube",color = skin ,position = (x,6,0))

    #Mouth

    for x in range(3,5):
        a = Entity(model="cube",color = mouth ,position = (x,2,0))

    #Eyes 

    a = Entity(model="cube",color = color.white ,position = (1,4,0))
    a = Entity(model="cube",color = eyes ,position = (2,4,0))

    a = Entity(model="cube",color = color.white ,position = (6,4,0))
    a = Entity(model="cube",color = eyes ,position = (5,4,0))


    #Hair
    for x in range(8):
        if x != 3 and x != 4 and x != 5 and x != 6:
            a = Entity(model="cube",color = hair ,position = (x,5,0))

    for x in range(8):
        if x != 4 and x != 5:
            a = Entity(model="cube",color = hair ,position = (x,6,0))

    for x in range(8):
        for y in range(2):
            a = Entity(model="cube",color = hair ,position = (x,7+y,0))

    EditorCamera()
    app.run()


