from ursina import *

def Magma_default():

    app = Ursina()


    #fila 0
    Entity(model='cube', color=color.brown, position=(0,0))
    Entity(model='cube', color=color.brown, position=(1,0))
    Entity(model='cube', color=color.brown, position=(2,0))
    Entity(model='cube', color=color.brown, position=(3,0))
    Entity(model='cube', color=color.brown, position=(4,0))
    Entity(model='cube', color=color.brown, position=(5,0))
    Entity(model='cube', color=color.brown, position=(6,0))
    Entity(model='cube', color=color.brown, position=(7,0))
    Entity(model='cube', color=color.brown, position=(8,0))
    #columna 0
    Entity(model='cube', color=color.brown, position=(0,1))
    Entity(model='cube', color=color.brown, position=(0,2))
    Entity(model='cube', color=color.brown, position=(0,3))
    Entity(model='cube', color=color.brown, position=(0,4))
    Entity(model='cube', color=color.brown, position=(0,5))
    Entity(model='cube', color=color.brown, position=(0,6))
    Entity(model='cube', color=color.brown, position=(0,7))
    Entity(model='cube', color=color.brown, position=(0,8))
    #columna 1
    Entity(model='cube', color=color.brown, position=(1,1))
    Entity(model='cube', color=color.brown, position=(1,2))
    Entity(model='cube', color=color.brown, position=(1,3))
    Entity(model='cube', color=color.orange, position=(1,4))
    Entity(model='cube', color=color.red, position=(1,5))
    Entity(model='cube', color=color.brown, position=(1,6))
    Entity(model='cube', color=color.brown, position=(1,7))
    Entity(model='cube', color=color.brown, position=(1,8))
    #columna 2
    Entity(model='cube', color=color.brown, position=(2,1))
    Entity(model='cube', color=color.brown, position=(2,2))
    Entity(model='cube', color=color.brown, position=(2,3))
    Entity(model='cube', color=color.yellow, position=(2,4))
    Entity(model='cube', color=color.red, position=(2,5))
    Entity(model='cube', color=color.brown, position=(2,6))
    Entity(model='cube', color=color.brown, position=(2,7))
    Entity(model='cube', color=color.brown, position=(2,8))
    #columna 3

    Entity(model='cube', color=color.brown, position=(3, 1))
    Entity(model='cube', color=color.brown, position=(3, 2))
    Entity(model='cube', color=color.brown, position=(3, 3))
    Entity(model='cube', color=color.brown, position=(3, 4))
    Entity(model='cube', color=color.brown, position=(3, 5))
    Entity(model='cube', color=color.brown, position=(3, 6))
    Entity(model='cube', color=color.brown, position=(3, 7))
    Entity(model='cube', color=color.brown, position=(3, 8))
    #columna 4

    Entity(model='cube', color=color.brown, position=(4, 1))
    Entity(model='cube', color=color.brown, position=(4, 2))
    Entity(model='cube', color=color.brown, position=(4, 3))
    Entity(model='cube', color=color.brown, position=(4, 4))
    Entity(model='cube', color=color.brown, position=(4, 5))
    Entity(model='cube', color=color.brown, position=(4, 6))
    Entity(model='cube', color=color.brown, position=(4, 7))
    Entity(model='cube', color=color.brown, position=(4, 8))
    #columna 5

    Entity(model='cube', color=color.brown, position=(5, 1))
    Entity(model='cube', color=color.brown, position=(5, 2))
    Entity(model='cube', color=color.brown, position=(5, 3))
    Entity(model='cube', color=color.brown, position=(5, 4))
    Entity(model='cube', color=color.brown, position=(5, 5))
    Entity(model='cube', color=color.brown, position=(5, 6))
    Entity(model='cube', color=color.brown, position=(5, 7))
    Entity(model='cube', color=color.brown, position=(5, 8))
    #columna 6

    Entity(model='cube', color=color.brown, position=(6, 1))
    Entity(model='cube', color=color.brown, position=(6, 2))
    Entity(model='cube', color=color.brown, position=(6, 3))
    Entity(model='cube', color=color.yellow, position=(6, 4))
    Entity(model='cube', color=color.red, position=(6, 5))
    Entity(model='cube', color=color.brown, position=(6, 6))
    Entity(model='cube', color=color.brown, position=(6, 7))
    Entity(model='cube', color=color.brown, position=(6, 8))
    #columna 7

    Entity(model='cube', color=color.brown, position=(7, 1))
    Entity(model='cube', color=color.brown, position=(7, 2))
    Entity(model='cube', color=color.brown, position=(7, 3))
    Entity(model='cube', color=color.orange, position=(7, 4))
    Entity(model='cube', color=color.red, position=(7, 5))
    Entity(model='cube', color=color.brown, position=(7, 6))
    Entity(model='cube', color=color.brown, position=(7, 7))
    Entity(model='cube', color=color.brown, position=(7, 8))

    #columna 8

    Entity(model='cube', color=color.brown, position=(8, 1))
    Entity(model='cube', color=color.brown, position=(8, 2))
    Entity(model='cube', color=color.brown, position=(8, 3))
    Entity(model='cube', color=color.brown, position=(8, 4))
    Entity(model='cube', color=color.brown, position=(8, 5))
    Entity(model='cube', color=color.brown, position=(8, 6))
    Entity(model='cube', color=color.brown, position=(8, 7))
    Entity(model='cube', color=color.brown, position=(8, 8))
    EditorCamera()

    app.run()

def Magma(primary_color,secondary_color):

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
    Entity(model='cube', color=primary_color, position=(8,0))
    #columna 0
    Entity(model='cube', color=primary_color, position=(0,1))
    Entity(model='cube', color=primary_color, position=(0,2))
    Entity(model='cube', color=primary_color, position=(0,3))
    Entity(model='cube', color=primary_color, position=(0,4))
    Entity(model='cube', color=primary_color, position=(0,5))
    Entity(model='cube', color=primary_color, position=(0,6))
    Entity(model='cube', color=primary_color, position=(0,7))
    Entity(model='cube', color=primary_color, position=(0,8))
    #columna 1
    Entity(model='cube', color=primary_color, position=(1,1))
    Entity(model='cube', color=primary_color, position=(1,2))
    Entity(model='cube', color=primary_color, position=(1,3))
    Entity(model='cube', color=color.orange, position=(1,4))
    Entity(model='cube', color=secondary_color, position=(1,5))
    Entity(model='cube', color=primary_color, position=(1,6))
    Entity(model='cube', color=primary_color, position=(1,7))
    Entity(model='cube', color=primary_color, position=(1,8))
    #columna 2
    Entity(model='cube', color=primary_color, position=(2,1))
    Entity(model='cube', color=primary_color, position=(2,2))
    Entity(model='cube', color=primary_color, position=(2,3))
    Entity(model='cube', color=color.yellow, position=(2,4))
    Entity(model='cube', color=secondary_color, position=(2,5))
    Entity(model='cube', color=primary_color, position=(2,6))
    Entity(model='cube', color=primary_color, position=(2,7))
    Entity(model='cube', color=primary_color, position=(2,8))
    #columna 3

    Entity(model='cube', color=primary_color, position=(3, 1))
    Entity(model='cube', color=primary_color, position=(3, 2))
    Entity(model='cube', color=primary_color, position=(3, 3))
    Entity(model='cube', color=primary_color, position=(3, 4))
    Entity(model='cube', color=primary_color, position=(3, 5))
    Entity(model='cube', color=primary_color, position=(3, 6))
    Entity(model='cube', color=primary_color, position=(3, 7))
    Entity(model='cube', color=primary_color, position=(3, 8))
    #columna 4

    Entity(model='cube', color=primary_color, position=(4, 1))
    Entity(model='cube', color=primary_color, position=(4, 2))
    Entity(model='cube', color=primary_color, position=(4, 3))
    Entity(model='cube', color=primary_color, position=(4, 4))
    Entity(model='cube', color=primary_color, position=(4, 5))
    Entity(model='cube', color=primary_color, position=(4, 6))
    Entity(model='cube', color=primary_color, position=(4, 7))
    Entity(model='cube', color=primary_color, position=(4, 8))
    #columna 5

    Entity(model='cube', color=primary_color, position=(5, 1))
    Entity(model='cube', color=primary_color, position=(5, 2))
    Entity(model='cube', color=primary_color, position=(5, 3))
    Entity(model='cube', color=primary_color, position=(5, 4))
    Entity(model='cube', color=primary_color, position=(5, 5))
    Entity(model='cube', color=primary_color, position=(5, 6))
    Entity(model='cube', color=primary_color, position=(5, 7))
    Entity(model='cube', color=primary_color, position=(5, 8))
    #columna 6

    Entity(model='cube', color=primary_color, position=(6, 1))
    Entity(model='cube', color=primary_color, position=(6, 2))
    Entity(model='cube', color=primary_color, position=(6, 3))
    Entity(model='cube', color=color.yellow, position=(6, 4))
    Entity(model='cube', color=secondary_color, position=(6, 5))
    Entity(model='cube', color=primary_color, position=(6, 6))
    Entity(model='cube', color=primary_color, position=(6, 7))
    Entity(model='cube', color=primary_color, position=(6, 8))
    #columna 7

    Entity(model='cube', color=primary_color, position=(7, 1))
    Entity(model='cube', color=primary_color, position=(7, 2))
    Entity(model='cube', color=primary_color, position=(7, 3))
    Entity(model='cube', color=color.orange, position=(7, 4))
    Entity(model='cube', color=secondary_color, position=(7, 5))
    Entity(model='cube', color=primary_color, position=(7, 6))
    Entity(model='cube', color=primary_color, position=(7, 7))
    Entity(model='cube', color=primary_color, position=(7, 8))

    #columna 8

    Entity(model='cube', color=primary_color, position=(8, 1))
    Entity(model='cube', color=primary_color, position=(8, 2))
    Entity(model='cube', color=primary_color, position=(8, 3))
    Entity(model='cube', color=primary_color, position=(8, 4))
    Entity(model='cube', color=primary_color, position=(8, 5))
    Entity(model='cube', color=primary_color, position=(8, 6))
    Entity(model='cube', color=primary_color, position=(8, 7))
    Entity(model='cube', color=primary_color, position=(8, 8))
    EditorCamera()

    app.run()

