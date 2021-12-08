from ursina import *


def Blaze_default():
    
    app = Ursina()

    #Skin 1
    for x in range(8):
        for y in range(2):
            b = Entity(model="cube",color = rgb(255,87,51) ,position = (x,y,1))

    b = Entity(model="cube",color = rgb(255,87,51) ,position = (7,2,1))

    #Skin 2

    for x in range(7):
        b = Entity(model="cube",color = rgb(255,195,0 ) ,position = (x,2,1))
        
    for x in range(8):
        if x != 1 and x != 2 and x != 5 and x != 6:
            b = Entity(model="cube",color = rgb(255,195,0 ) ,position = (x,3,1))

    for x in range(8):
        for y in range(4):
            b = Entity(model="cube",color = rgb(255,195,0 ) ,position = (x,4+y,1))

    #Eyes

    b = Entity(model="cube",color = rgb(255,219,102) ,position = (1,3,1))
    b = Entity(model="cube",color = color.black ,position = (2,3,1))

    b = Entity(model="cube",color = rgb(255,219,102) ,position = (6,3,1))
    b = Entity(model="cube",color = color.black ,position = (5,3,1))

    EditorCamera()
    app.run()

def Blaze(primary_color,secondary_color):
    app = Ursina()

    #Skin 1
    for x in range(8):
        for y in range(2):
            b = Entity(model="cube",color = secondary_color ,position = (x,y,1))

    b = Entity(model="cube",color = secondary_color ,position = (7,2,1))

    #Skin 2

    for x in range(7):
        b = Entity(model="cube",color = primary_color ,position = (x,2,1))
        
    for x in range(8):
        if x != 1 and x != 2 and x != 5 and x != 6:
            b = Entity(model="cube",color = primary_color ,position = (x,3,1))

    for x in range(8):
        for y in range(4):
            b = Entity(model="cube",color = primary_color ,position = (x,4+y,1))

    #Eyes

    b = Entity(model="cube",color = rgb(255,219,102) ,position = (1,3,1))
    b = Entity(model="cube",color = color.black ,position = (2,3,1))

    b = Entity(model="cube",color = rgb(255,219,102) ,position = (6,3,1))
    b = Entity(model="cube",color = color.black ,position = (5,3,1))

    EditorCamera()
    app.run()

