from ursina import *
def calamar_predeterm():
    app = Ursina()


#fila 0

    Entity(model='cube', color=color.blue, position=(1,0))
    Entity(model='cube', color=color.blue, position=(2,0))
    Entity(model='cube', color=color.blue, position=(3,0))
    Entity(model='cube', color=color.blue, position=(4,0))
    Entity(model='cube', color=color.blue, position=(5,0))
    Entity(model='cube', color=color.blue, position=(6,0))
    Entity(model='cube', color=color.blue, position=(7,0))
    Entity(model='cube', color=color.blue, position=(8,0))

    #columna 1
    Entity(model='cube', color=color.blue, position=(1,1))
    Entity(model='cube', color=color.blue, position=(1,2))
    Entity(model='cube', color=color.blue,position=(1,3))
    Entity(model='cube', color=color.blue, position=(1,4))
    Entity(model='cube', color=color.blue, position=(1,5))
    Entity(model='cube', color=color.blue, position=(1,6))
    Entity(model='cube', color=color.blue, position=(1,7))

    #columna 2
    Entity(model='cube', color=color.blue, position=(2,1))
    Entity(model='cube', color=color.azure, position=(2,2))
    Entity(model='cube', color=color.azure, position=(2,3))
    Entity(model='cube', color=color.white, position=(2,4))
    Entity(model='cube', color=color.black, position=(2,5))
    Entity(model='cube', color=color.blue, position=(2,6))
    Entity(model='cube', color=color.blue, position=(2,7))

    #columna 3

    Entity(model='cube', color=color.azure, position=(3, 1))
    Entity(model='cube', color=color.azure, position=(3, 2))
    Entity(model='cube', color=color.azure, position=(3, 3))
    Entity(model='cube', color=color.white, position=(3, 4))
    Entity(model='cube', color=color.white, position=(3, 5))
    Entity(model='cube', color=color.azure, position=(3, 6))
    Entity(model='cube', color=color.blue, position=(3, 7))

    #columna 4

    Entity(model='cube', color=color.azure, position=(4, 1))
    Entity(model='cube', color=color.azure, position=(4, 2))
    Entity(model='cube', color=color.azure, position=(4, 3))
    Entity(model='cube', color=color.azure, position=(4, 4))
    Entity(model='cube', color=color.azure, position=(4, 5))
    Entity(model='cube', color=color.azure, position=(4, 6))
    Entity(model='cube', color=color.blue, position=(4, 7))

    #columna 5

    Entity(model='cube', color=color.azure, position=(5, 1))
    Entity(model='cube', color=color.azure, position=(5, 2))
    Entity(model='cube', color=color.azure, position=(5, 3))
    Entity(model='cube', color=color.azure, position=(5, 4))
    Entity(model='cube', color=color.azure, position=(5, 5))
    Entity(model='cube', color=color.azure, position=(5, 6))
    Entity(model='cube', color=color.blue, position=(5, 7))

    #columna 6

    Entity(model='cube', color=color.azure, position=(6, 1))
    Entity(model='cube', color=color.azure, position=(6, 2))
    Entity(model='cube', color=color.azure, position=(6, 3))
    Entity(model='cube', color=color.white, position=(6, 4))
    Entity(model='cube', color=color.white, position=(6, 5))
    Entity(model='cube', color=color.azure, position=(6, 6))
    Entity(model='cube', color=color.blue, position=(6, 7))

    #columna 7

    Entity(model='cube', color=color.blue, position=(7, 1))
    Entity(model='cube', color=color.azure, position=(7, 2))
    Entity(model='cube', color=color.azure, position=(7, 3))
    Entity(model='cube', color=color.white, position=(7, 4))
    Entity(model='cube', color=color.black, position=(7, 5))
    Entity(model='cube', color=color.blue, position=(7, 6))
    Entity(model='cube', color=color.blue, position=(7, 7))


    #columna 8

    Entity(model='cube', color=color.blue, position=(8, 1))
    Entity(model='cube', color=color.blue, position=(8, 2))
    Entity(model='cube', color=color.blue, position=(8, 3))
    Entity(model='cube', color=color.blue, position=(8, 4))
    Entity(model='cube', color=color.blue, position=(8, 5))
    Entity(model='cube', color=color.blue, position=(8, 6))
    Entity(model='cube', color=color.blue, position=(8, 7))

    EditorCamera()

    app.run()
print(calamar_predeterm())

# se le pide al usuario que ingrese su color de preferencia


def calamar(primary_color, secondary_color):
    app = Ursina()

    Entity(model='cube', color=color.primary_color, position=(1, 0))
    Entity(model='cube', color=color.primary_color, position=(2, 0))
    Entity(model='cube', color=color.primary_color, position=(3, 0))
    Entity(model='cube', color=color.primary_color, position=(4, 0))
    Entity(model='cube', color=color.primary_color, position=(5, 0))
    Entity(model='cube', color=color.primary_color, position=(6, 0))
    Entity(model='cube', color=color.primary_color, position=(7, 0))
    Entity(model='cube', color=color.primary_color, position=(8, 0))

    # columna 1
    Entity(model='cube', color=color.primary_color, position=(1, 1))
    Entity(model='cube', color=color.primary_color, position=(1, 2))
    Entity(model='cube', color=color.primary_color, position=(1, 3))
    Entity(model='cube', color=color.primary_color, position=(1, 4))
    Entity(model='cube', color=color.primary_color, position=(1, 5))
    Entity(model='cube', color=color.primary_color, position=(1, 6))
    Entity(model='cube', color=color.primary_color, position=(1, 7))

    # columna 2
    Entity(model='cube', color=color.primary_color, position=(2, 1))
    Entity(model='cube', color=color.secondary_color, position=(2, 2))
    Entity(model='cube', color=color.secondary_color, position=(2, 3))
    Entity(model='cube', color=color.white, position=(2, 4))
    Entity(model='cube', color=color.black, position=(2, 5))
    Entity(model='cube', color=color.primary_color, position=(2, 6))
    Entity(model='cube', color=color.primary_color, position=(2, 7))

    # columna 3

    Entity(model='cube', color=color.secondary_color, position=(3, 1))
    Entity(model='cube', color=color.secondary_color, position=(3, 2))
    Entity(model='cube', color=color.secondary_color, position=(3, 3))
    Entity(model='cube', color=color.white, position=(3, 4))
    Entity(model='cube', color=color.white, position=(3, 5))
    Entity(model='cube', color=color.secondary_color, position=(3, 6))
    Entity(model='cube', color=color.primary_color, position=(3, 7))

    # columna 4

    Entity(model='cube', color=color.secondary_color, position=(4, 1))
    Entity(model='cube', color=color.secondary_color, position=(4, 2))
    Entity(model='cube', color=color.secondary_color, position=(4, 3))
    Entity(model='cube', color=color.secondary_color, position=(4, 4))
    Entity(model='cube', color=color.secondary_color, position=(4, 5))
    Entity(model='cube', color=color.secondary_color, position=(4, 6))
    Entity(model='cube', color=color.primary_color, position=(4, 7))

    # columna 5

    Entity(model='cube', color=color.secondary_color, position=(5, 1))
    Entity(model='cube', color=color.secondary_color, position=(5, 2))
    Entity(model='cube', color=color.secondary_color, position=(5, 3))
    Entity(model='cube', color=color.secondary_color, position=(5, 4))
    Entity(model='cube', color=color.secondary_color, position=(5, 5))
    Entity(model='cube', color=color.secondary_color, position=(5, 6))
    Entity(model='cube', color=color.primary_color, position=(5, 7))

    # columna 6

    Entity(model='cube', color=color.secondary_color, position=(6, 1))
    Entity(model='cube', color=color.secondary_color, position=(6, 2))
    Entity(model='cube', color=color.secondary_color, position=(6, 3))
    Entity(model='cube', color=color.white, position=(6, 4))
    Entity(model='cube', color=color.white, position=(6, 5))
    Entity(model='cube', color=color.secondary_color, position=(6, 6))
    Entity(model='cube', color=color.primary_color, position=(6, 7))

    # columna 7

    Entity(model='cube', color=color.primary_color, position=(7, 1))
    Entity(model='cube', color=color.secondary_color, position=(7, 2))
    Entity(model='cube', color=color.secondary_color, position=(7, 3))
    Entity(model='cube', color=color.white, position=(7, 4))
    Entity(model='cube', color=color.black, position=(7, 5))
    Entity(model='cube', color=color.primary_color, position=(7, 6))
    Entity(model='cube', color=color.primary_color, position=(7, 7))

    # columna 8

    Entity(model='cube', color=color.primary_color, position=(8, 1))
    Entity(model='cube', color=color.primary_color, position=(8, 2))
    Entity(model='cube', color=color.primary_color, position=(8, 3))
    Entity(model='cube', color=color.primary_color, position=(8, 4))
    Entity(model='cube', color=color.primary_color, position=(8, 5))
    Entity(model='cube', color=color.primary_color, position=(8, 6))
    Entity(model='cube', color=color.primary_color, position=(8, 7))

    EditorCamera()

    app.run()
