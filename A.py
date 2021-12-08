from ursina import *

app = Ursina()
#NARIZ
b = Entity(model="cube",color = color.black ,position = (3,3,0))
b = Entity(model="cube",color = color.black ,position = (4,3,0))
#boca
b = Entity(model="cube",color = color.black ,position = (4,2,0))
b = Entity(model="cube",color = color.black ,position = (4,1,0))
b = Entity(model="cube",color = color.black ,position = (5,2,0))
b = Entity(model="cube",color = color.black ,position = (3,2,0))
b = Entity(model="cube",color = color.black ,position = (2,2,0))
b = Entity(model="cube",color = color.black ,position = (3,1,0))
b = Entity(model="cube",color = color.black ,position = (2,1,0))
b = Entity(model="cube",color = color.black ,position = (5,1,0))
b = Entity(model="cube",color = color.black ,position = (5,0,0))
b = Entity(model="cube",color = color.black ,position = (2,0,0))
#OJOS
b = Entity(model="cube",color = color.black ,position = (1,5,0))
b = Entity(model="cube",color = color.black ,position = (2,5,0))
b = Entity(model="cube",color = color.black ,position = (2,4,0))
b = Entity(model="cube",color = color.black ,position = (1,4,0))
b = Entity(model="cube",color = color.black ,position = (5,5,0))
b = Entity(model="cube",color = color.black ,position = (6,5,0))
b = Entity(model="cube",color = color.black ,position = (6,4,0))
b = Entity(model="cube",color = color.black ,position = (5,4,0))
#rostro de fondo

for y in range(0,8):
    b = Entity(model="cube",color = rgb(0,187,45) ,position = (0,y,0))
    b = Entity(model="cube", color=rgb(0, 187, 45), position=(7, y, 0))
for y in range(0, 4):
    b = Entity(model="cube", color=rgb(0, 187, 45), position=(1, y, 0))
    b = Entity(model="cube", color=rgb(0, 187, 45), position=(6, y, 0))
for x in range (3,5):
    b = Entity(model="cube",color = rgb(0,187,45) ,position = (x,0,0))
for x in range (1,7):
    b = Entity(model="cube",color = rgb(0,187,45) ,position = (x,7,0))
    b = Entity(model="cube", color=rgb(0, 187, 45), position=(x, 6, 0))

b = Entity(model="cube",color = rgb(0, 187, 45) ,position = (3,5,0))
b = Entity(model="cube",color = rgb(0, 187, 45) ,position = (4,5,0))
b = Entity(model="cube",color = rgb(0, 187, 45) ,position = (3,4,0))
b = Entity(model="cube",color = rgb(0, 187, 45) ,position = (4,4,0))
b = Entity(model="cube",color = rgb(0, 187, 45) ,position = (2,3,0))
b = Entity(model="cube",color = rgb(0, 187, 45) ,position = (5,3,0))
EditorCamera()
app.run()