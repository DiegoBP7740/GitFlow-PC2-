from ursina import *
def Creeper_default():
    app = Ursina()
    for y in range(0,8):
        b = Entity(model="cube", color=rgb(84, 197, 113), position=(0, y, 0))
        b = Entity(model="cube", color=rgb(84, 197, 113), position=(7, y, 0))
    for y in range(0,3):
        b = Entity(model="cube", color=rgb(84, 197, 113), position=(1, y, 0))
        b = Entity(model="cube", color=rgb(84, 197, 113), position=(2, y, 0))
        b = Entity(model="cube", color=rgb(84, 197, 113), position=(5, y, 0))
        b = Entity(model="cube", color=rgb(84, 197, 113), position=(6, y, 0))
    for y in range(4,8):
        b = Entity(model="cube", color=rgb(84, 197, 113), position=(1, y, 0))
        b = Entity(model="cube", color=rgb(84, 197, 113), position=(2, y, 0))
        b = Entity(model="cube", color=rgb(84, 197, 113), position=(5, y, 0))
        b = Entity(model="cube", color=rgb(84, 197, 113), position=(6, y, 0))
    for y in range(3,8):
        b = Entity(model="cube", color=rgb(84, 197, 113), position=(3, y, 0))
        b = Entity(model="cube", color=rgb(84, 197, 113), position=(4, y, 0))
    for y in range(0,2):
        b = Entity(model="cube", color=rgb(84, 197, 113), position=(3, y, 0))
        b = Entity(model="cube", color=rgb(84, 197, 113), position=(4, y, 0))
    #ojos
    b = Entity(model="cube", color=color.black, position=(1, 3, 0))
    b = Entity(model="cube", color=color.black, position=(2, 3, 0))
    b = Entity(model="cube", color=color.black, position=(5, 3, 0))
    b = Entity(model="cube", color=color.black, position=(6, 3, 0))

    b = Entity(model="cube", color=rgb(0,143,57), position=(3, 2, 0))
    b = Entity(model="cube", color=rgb(0,143,57), position=(4, 2, 0))
    EditorCamera()
    app.run()
def Creeper(primary_color, secondary_color):
    app = Ursina()
    for y in range(0, 8):
        b = Entity(model="cube", color=primary_color, position=(0, y, 0))
        b = Entity(model="cube", color=primary_color, position=(7, y, 0))
    for y in range(0, 3):
        b = Entity(model="cube", color=primary_color, position=(1, y, 0))
        b = Entity(model="cube", color=primary_color, position=(2, y, 0))
        b = Entity(model="cube", color=primary_color, position=(5, y, 0))
        b = Entity(model="cube", color=primary_color, position=(6, y, 0))
    for y in range(4, 8):
        b = Entity(model="cube", color=primary_color, position=(1, y, 0))
        b = Entity(model="cube", color=primary_color, position=(2, y, 0))
        b = Entity(model="cube", color=primary_color, position=(5, y, 0))
        b = Entity(model="cube", color=primary_color, position=(6, y, 0))
    for y in range(3, 8):
        b = Entity(model="cube", color=primary_color, position=(3, y, 0))
        b = Entity(model="cube", color=primary_color, position=(4, y, 0))
    for y in range(0, 2):
        b = Entity(model="cube", color=primary_color, position=(3, y, 0))
        b = Entity(model="cube", color=primary_color, position=(4, y, 0))
    # ojos
    b = Entity(model="cube", color=color.black, position=(1, 3, 0))
    b = Entity(model="cube", color=color.black, position=(2, 3, 0))
    b = Entity(model="cube", color=color.black, position=(5, 3, 0))
    b = Entity(model="cube", color=color.black, position=(6, 3, 0))

    b = Entity(model="cube", color=secondary_color, position=(3, 2, 0))
    b = Entity(model="cube", color=secondary_color, position=(4, 2, 0))
    EditorCamera()
    app.run()