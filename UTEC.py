from ursina import*

def UTEC():

    app = Ursina()

    Sky()

    e = Entity(model='cube', position=(0,0,1), scale=8, texture='UTEC.jpg')

    EditorCamera()

    app.run()