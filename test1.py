from ursina import *

app = Ursina()


imagen_3d = Entity(model="cube",position=(0,0,0),texture="PRO.jpg")

EditorCamera()
app.run()