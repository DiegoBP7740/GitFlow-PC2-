from ursina import *

app = Ursina()
#fondo de cara
for y in range(0,6):
    b = Entity(model="cube", color=rgb(130,137,143), position=(0, y, 0))
    b = Entity(model="cube", color=rgb(130,137,143), position=(7, y, 0))
for y in range(0,3):
    b = Entity(model="cube", color=rgb(130,137,143), position=(1, y, 0))
    b = Entity(model="cube", color=rgb(130,137,143), position=(2, y, 0))
    b = Entity(model="cube", color=rgb(130,137,143), position=(5, y, 0))
    b = Entity(model="cube", color=rgb(130, 137, 143), position=(6, y, 0))
for y in range(4,8):
    b = Entity(model="cube", color=rgb(130, 137, 143), position=(1, y, 0))
    b = Entity(model="cube", color=rgb(130, 137, 143), position=(2, y, 0))
for y in range(4,7):
    b = Entity(model="cube", color=rgb(130, 137, 143), position=(3, y, 0))
for y in range(4,6):
    b = Entity(model="cube", color=rgb(130, 137, 143), position=(4, y, 0))
    b = Entity(model="cube", color=rgb(130, 137, 143), position=(5, y, 0))
    b = Entity(model="cube", color=rgb(130, 137, 143), position=(6, y, 0))
    b = Entity(model="cube", color=rgb(130, 137, 143), position=(7, y, 0))
for y in range(0,2):
    b = Entity(model="cube", color=rgb(130, 137, 143), position=(4, y, 0))
    b = Entity(model="cube", color=rgb(130, 137, 143), position=(3, y, 0))
b = Entity(model="cube", color=rgb(130, 137, 143), position=(3, 3, 0))
b = Entity(model="cube", color=rgb(130, 137, 143), position=(4, 3, 0))

#cabello
for x in range(3,8):
    b = Entity(model="cube", color=rgb(250, 210, 1), position=(x,6, 0))
for x in range(2,8):
    b = Entity(model="cube", color=rgb(250, 210, 1), position=(x, 7, 0))
for y in range(6,8):
    b = Entity(model="cube", color=rgb(250, 210, 1), position=(0, y, 0))
#ojos
b = Entity(model="cube", color=color.black, position=(1, 3, 0))
b = Entity(model="cube", color=color.black, position=(2, 3, 0))
b = Entity(model="cube", color=color.black, position=(5, 3, 0))
b = Entity(model="cube", color=color.black, position=(6, 3, 0))
#nariz
b = Entity(model="cube", color=rgb(71, 75,78 ), position=(3, 2, 0))
b = Entity(model="cube", color=rgb(71, 75,78), position=(4, 2, 0))
EditorCamera()
app.run()
