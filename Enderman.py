from ursina import *
def Enderman_default():
    app = Ursina()
    # fondo
    for y in range(0,3):
        b = Entity(model="cube",color =color.black ,position = (0,y,0))
        b = Entity(model="cube", color=color.black, position=(1, y, 0))
        b = Entity(model="cube", color=color.black, position=(2, y, 0))
        b = Entity(model="cube", color=color.black, position=(5, y, 0))
        b = Entity(model="cube", color=color.black, position=(6, y, 0))
        b = Entity(model="cube", color=color.black, position=(7, y, 0))
    for y in range(4,8):
        b = Entity(model="cube", color=color.black, position=(0, y, 0))
        b = Entity(model="cube", color=color.black, position=(1, y, 0))
        b = Entity(model="cube", color=color.black, position=(2, y, 0))
        b = Entity(model="cube", color=color.black, position=(5, y, 0))
        b = Entity(model="cube", color=color.black, position=(6, y, 0))
        b = Entity(model="cube", color=color.black, position=(7, y, 0))
    for y in range(0,8):
        b = Entity(model="cube", color=color.black, position=(3, y, 0))
        b = Entity(model="cube", color=color.black, position=(4, y, 0))
    #ojos
    b = Entity(model="cube", color=color.white, position=(0, 3, 0))
    b = Entity(model="cube", color=rgb(120,40,140), position=(1, 3, 0))
    b = Entity(model="cube", color=color.white, position=(2, 3, 0))
    b= Entity(model="cube", color=color.white, position=(5, 3, 0))
    b = Entity(model="cube", color=rgb(120,40,140), position=(6, 3, 0))
    b= Entity(model="cube", color=color.white, position=(7, 3, 0))
    EditorCamera()
    app.run()

    
def Enderman(primary_color, secondary_color):
    app = Ursina()
    for y in range(0,3):
        b = Entity(model="cube",color =primary_color ,position = (0,y,0))
        b = Entity(model="cube", color=primary_color, position=(1, y, 0))
        b = Entity(model="cube", color=primary_color, position=(2, y, 0))
        b = Entity(model="cube", color=primary_color, position=(5, y, 0))
        b = Entity(model="cube", color=primary_color, position=(6, y, 0))
        b = Entity(model="cube", color=primary_color, position=(7, y, 0))
    for y in range(4,8):
        b = Entity(model="cube", color=primary_color, position=(0, y, 0))
        b = Entity(model="cube", color=primary_color, position=(1, y, 0))
        b = Entity(model="cube", color=primary_color, position=(2, y, 0))
        b = Entity(model="cube", color=primary_color, position=(5, y, 0))
        b = Entity(model="cube", color=primary_color, position=(6, y, 0))
        b = Entity(model="cube", color=primary_color, position=(7, y, 0))
    for y in range(0,8):
        b = Entity(model="cube", color=primary_color, position=(3, y, 0))
        b = Entity(model="cube", color=primary_color, position=(4, y, 0))
    #ojos
    b = Entity(model="cube", color=color.white, position=(0, 3, 0))
    b = Entity(model="cube", color=secondary_color, position=(1, 3, 0))
    b = Entity(model="cube", color=color.white, position=(2, 3, 0))
    b= Entity(model="cube", color=color.white, position=(5, 3, 0))
    b = Entity(model="cube", color=secondary_color, position=(6, 3, 0))
    b= Entity(model="cube", color=color.white, position=(7, 3, 0))
    EditorCamera()
    app.run()