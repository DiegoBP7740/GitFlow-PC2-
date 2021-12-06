from ursina import *

app = Ursina()


#cabello

for x in range(8):
    for y in range(2):
        c1 = Entity(model="cube",color = rgb(249,174,43),position = (x,6+y,0))

for x in range(3):
    for y in range(2):
        c2 = Entity(model="cube",color = rgb(249,174,43),position = (x,4+y,0))

c3 = Entity(model="cube",color = rgb(249,174,43),position = (3,5,0))

for x in range(2):
    for y in range(1):
        c4 = Entity(model="cube",color = rgb(249,174,43),position = (6+x,5+y,0))

c5 = Entity(model="cube",color = rgb(249,174,43),position = (7,4,0))

1
#ojos
ojo_I = Entity(model="cube",color = rgb(256,256,256),position = (1,3,0))
pupila_I = Entity(model="cube",color = rgb(25,99,252),position = (2,3,0))

ojo_D = Entity(model="cube",color = rgb(256,256,256),position = (6,3,0))
pupila_D = Entity(model="cube",color = rgb(25,99,252),position = (5,3,0))

#piel

for x in range(8):
    for y in range(8):
        piel = Entity(model="cube",color = rgb(255,226,164),position = (x,y,0))

#boca
for x in range(2):
    for y in range(1):
        piel = Entity(model="cube",color = rgb(251,166,226),position = (x+3,y+1,0))


EditorCamera()
app.run()