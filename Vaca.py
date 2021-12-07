from ursina import *

app = Ursina()
# 0 1 2 3 4 5 6 7 

#CABEZA VACA
for y in range(4):
    b = Entity(model="cube",color = rgb(70,42,42),position = (0,y,0))
    b = Entity(model="cube",color = rgb(70,42,42),position = (7,y,0))
for x in range (1,7):
    b = Entity(model="cube",color = rgb(70,42,42) ,position = (x,3,0))
for y in range(3,7):
    b = Entity(model="cube",color = rgb(70,42,42), position = (2,y,0))
for x in range(4,6):
    b = Entity(model="cube",color = rgb(70,42,42), position = (x,4,0))
b = Entity(model="cube",color = rgb(70,42,42), position = (5,5,0))

#PUPILA IZQUIERDA
for y in range(4,6):
    if y == 4:
        b = Entity(model="cube",color = color.white, position = (6,y,0))
    elif y == 5:
        for i in range(6,8):
            b = Entity(model="cube",color = color.white, position = (i,y,0))
b = Entity(model="cube",color = color.black , position = (7,4,0))

#PUPILA DERECHA
b = Entity(model="cube",color = color.black , position = (0,4,0))
for y in range(4,6):
    if y == 4:
        b = Entity(model="cube",color = color.white, position = (1,y,0))
    elif y == 5:
        for i in range(2):
            b = Entity(model="cube",color = color.white, position = (i,y,0))

#PARTE SUPERIOR DE VACA
base = 3
altu = 4
for i in range(3):
    for y in range (altu,8):
        b = Entity(model="cube",color = color.white , position = (base,y,0))
    altu+=1
    base+=1
for i in range (2):
    for x in range(6,8):
        for y in range (6,8):
         b = Entity(model="cube",color = rgb(70,42,42) , position = (x,y,0))
for i in range (2):
    for x in range(2):
        for y in range (6,8):
         b = Entity(model="cube",color = rgb(70,42,42) , position = (x,y,0))
b =  Entity(model="cube",color = rgb(70,42,42) , position = (2,7,0))

#alrededor de boca
b = Entity(model="cube",color = color.white,position = (1,0,0))
b = Entity(model="cube",color = color.white,position = (6,0,0))
b = Entity(model="cube",color = color.white,position = (1,1,0))
b = Entity(model="cube",color = color.white,position = (6,1,0))


#parte superior de boca
for x in range (4):
    b = Entity(model="cube",color = color.white,position = (2+x,2,0))

for x in range (3,5):
    b = Entity(model="cube",color = rgb(169,169,169),position = (x,0,0))
b = Entity(model="cube",color = rgb(105, 105, 105),position = (2,0,0))
b = Entity(model="cube",color = rgb(105, 105, 105),position = (5,0,0))
b = Entity(model="cube",color = color.black ,position = (2,1,0))
b = Entity(model="cube",color = color.black ,position = (5,1,0))
for x in range (3,5):
    b = Entity(model="cube",color = rgb(105, 105, 105),position = (x,1,0))
b  = Entity(model="cube",color =rgb(70,42,42) ,position = (1,2,0))
b  = Entity(model="cube",color =rgb(70,42,42) ,position = (6,2,0))

EditorCamera()
app.run()
