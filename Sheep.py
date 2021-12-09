from ursina import *

def Sheep_default():
    app = Ursina()

    #fila 0
    Entity(model='cube', color=color.white, position=(0,0))
    Entity(model='cube', color=color.white, position=(1,0))
    Entity(model='cube', color=color.white, position=(2,0))
    Entity(model='cube', color=color.white, position=(3,0))
    Entity(model='cube', color=color.white, position=(4,0))
    Entity(model='cube', color=color.white, position=(5,0))
    Entity(model='cube', color=color.white, position=(6,0))
    Entity(model='cube', color=color.white, position=(7,0))

    #columna 0
    Entity(model='cube', color=color.white, position=(0,1))
    Entity(model='cube', color=color.white, position=(0,2))
    Entity(model='cube', color=color.white, position=(0,3))
    Entity(model='cube', color=color.white, position=(0,4))
    Entity(model='cube', color=color.white, position=(0,5))
    Entity(model='cube', color=color.white, position=(0,6))
    Entity(model='cube', color=color.white, position=(0,7))

    #columna 1
    Entity(model='cube', color=color.white, position=(1,1))
    Entity(model='cube', color=color.white, position=(1,2))
    Entity(model='cube', color=color.orange, position=(1,3))
    Entity(model='cube', color=color.black, position=(1,4))
    Entity(model='cube', color=color.orange, position=(1,5))
    Entity(model='cube', color=color.white, position=(1,6))
    Entity(model='cube', color=color.white, position=(1,7))

    #columna 2
    Entity(model='cube', color=color.orange, position=(2,1))
    Entity(model='cube', color=color.orange, position=(2,2))
    Entity(model='cube', color=color.orange, position=(2,3))
    Entity(model='cube', color=color.white, position=(2,4))
    Entity(model='cube', color=color.orange, position=(2,5))
    Entity(model='cube', color=color.white, position=(2,6))
    Entity(model='cube', color=color.white, position=(2,7))

    #columna 3

    Entity(model='cube', color=color.pink, position=(3, 1))
    Entity(model='cube', color=color.magenta, position=(3, 2))
    Entity(model='cube', color=color.orange, position=(3, 3))
    Entity(model='cube', color=color.orange, position=(3, 4))
    Entity(model='cube', color=color.orange, position=(3, 5))
    Entity(model='cube', color=color.white, position=(3, 6))
    Entity(model='cube', color=color.white, position=(3, 7))

    #columna 4

    Entity(model='cube', color=color.pink, position=(4, 1))
    Entity(model='cube', color=color.magenta, position=(4, 2))
    Entity(model='cube', color=color.orange, position=(4, 3))
    Entity(model='cube', color=color.orange, position=(4, 4))
    Entity(model='cube', color=color.orange, position=(4, 5))
    Entity(model='cube', color=color.white, position=(4, 6))
    Entity(model='cube', color=color.white, position=(4, 7))

    #columna 5

    Entity(model='cube', color=color.orange, position=(5, 1))
    Entity(model='cube', color=color.orange, position=(5, 2))
    Entity(model='cube', color=color.orange, position=(5, 3))
    Entity(model='cube', color=color.white, position=(5, 4))
    Entity(model='cube', color=color.orange, position=(5, 5))
    Entity(model='cube', color=color.white, position=(5, 6))
    Entity(model='cube', color=color.white, position=(5, 7))

    #columna 6

    Entity(model='cube', color=color.white, position=(6, 1))
    Entity(model='cube', color=color.white, position=(6, 2))
    Entity(model='cube', color=color.orange, position=(6, 3))
    Entity(model='cube', color=color.black, position=(6, 4))
    Entity(model='cube', color=color.orange, position=(6, 5))
    Entity(model='cube', color=color.white, position=(6, 6))
    Entity(model='cube', color=color.white, position=(6, 7))

    #columna 7

    Entity(model='cube', color=color.white, position=(7, 1))
    Entity(model='cube', color=color.white, position=(7, 2))
    Entity(model='cube', color=color.white, position=(7, 3))
    Entity(model='cube', color=color.white, position=(7, 4))
    Entity(model='cube', color=color.white, position=(7, 5))
    Entity(model='cube', color=color.white, position=(7, 6))
    Entity(model='cube', color=color.white, position=(7, 7))


    #columna 8


    EditorCamera()

    app.run()
    

def Sheep(primary_color,secondary_color):
    app = Ursina()

    #fila 0
    Entity(model='cube', color=primary_color, position=(0,0))
    Entity(model='cube', color=primary_color, position=(1,0))
    Entity(model='cube', color=primary_color, position=(2,0))
    Entity(model='cube', color=primary_color, position=(3,0))
    Entity(model='cube', color=primary_color, position=(4,0))
    Entity(model='cube', color=primary_color, position=(5,0))
    Entity(model='cube', color=primary_color, position=(6,0))
    Entity(model='cube', color=primary_color, position=(7,0))

    #columna 0
    Entity(model='cube', color=primary_color, position=(0,1))
    Entity(model='cube', color=primary_color, position=(0,2))
    Entity(model='cube', color=primary_color, position=(0,3))
    Entity(model='cube', color=primary_color, position=(0,4))
    Entity(model='cube', color=primary_color, position=(0,5))
    Entity(model='cube', color=primary_color, position=(0,6))
    Entity(model='cube', color=primary_color, position=(0,7))

    #columna 1
    Entity(model='cube', color=primary_color, position=(1,1))
    Entity(model='cube', color=primary_color, position=(1,2))
    Entity(model='cube', color=secondary_color, position=(1,3))
    Entity(model='cube', color=color.black, position=(1,4))
    Entity(model='cube', color=secondary_color, position=(1,5))
    Entity(model='cube', color=primary_color, position=(1,6))
    Entity(model='cube', color=primary_color, position=(1,7))

    #columna 2
    Entity(model='cube', color=secondary_color, position=(2,1))
    Entity(model='cube', color=secondary_color, position=(2,2))
    Entity(model='cube', color=secondary_color, position=(2,3))
    Entity(model='cube', color=color.white, position=(2,4))
    Entity(model='cube', color=secondary_color, position=(2,5))
    Entity(model='cube', color=primary_color, position=(2,6))
    Entity(model='cube', color=primary_color, position=(2,7))

    #columna 3

    Entity(model='cube', color=color.pink, position=(3, 1))
    Entity(model='cube', color=color.magenta, position=(3, 2))
    Entity(model='cube', color=secondary_color, position=(3, 3))
    Entity(model='cube', color=secondary_color, position=(3, 4))
    Entity(model='cube', color=secondary_color, position=(3, 5))
    Entity(model='cube', color=primary_color, position=(3, 6))
    Entity(model='cube', color=primary_color, position=(3, 7))

    #columna 4

    Entity(model='cube', color=color.pink, position=(4, 1))
    Entity(model='cube', color=color.magenta, position=(4, 2))
    Entity(model='cube', color=secondary_color, position=(4, 3))
    Entity(model='cube', color=secondary_color, position=(4, 4))
    Entity(model='cube', color=secondary_color, position=(4, 5))
    Entity(model='cube', color=primary_color, position=(4, 6))
    Entity(model='cube', color=primary_color, position=(4, 7))

    #columna 5

    Entity(model='cube', color=secondary_color, position=(5, 1))
    Entity(model='cube', color=secondary_color, position=(5, 2))
    Entity(model='cube', color=secondary_color, position=(5, 3))
    Entity(model='cube', color=color.white, position=(5, 4))
    Entity(model='cube', color=secondary_color, position=(5, 5))
    Entity(model='cube', color=primary_color, position=(5, 6))
    Entity(model='cube', color=primary_color, position=(5, 7))

    #columna 6

    Entity(model='cube', color=primary_color, position=(6, 1))
    Entity(model='cube', color=primary_color, position=(6, 2))
    Entity(model='cube', color=secondary_color, position=(6, 3))
    Entity(model='cube', color=color.black, position=(6, 4))
    Entity(model='cube', color=secondary_color, position=(6, 5))
    Entity(model='cube', color=primary_color, position=(6, 6))
    Entity(model='cube', color=primary_color, position=(6, 7))

    #columna 7

    Entity(model='cube', color=primary_color, position=(7, 1))
    Entity(model='cube', color=primary_color, position=(7, 2))
    Entity(model='cube', color=primary_color, position=(7, 3))
    Entity(model='cube', color=primary_color, position=(7, 4))
    Entity(model='cube', color=primary_color, position=(7, 5))
    Entity(model='cube', color=primary_color, position=(7, 6))
    Entity(model='cube', color=primary_color, position=(7, 7))


    #columna 8


    EditorCamera()

    app.run()    
