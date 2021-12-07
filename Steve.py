from ursina import *

app = Ursina()

#0 1 2 3 4 5 6 
#rostro
#color.red

#rostro lado
for x in range(2):
    b = Entity(model="cube",color = rgb(220,118,51) ,position = (x,0,0))
    b = Entity(model="cube",color = rgb(220,118,51) ,position = (x+6,0,0))

#Boca
for x in range (2,6):
    b = Entity(model="cube",color = rgb(70,42,42) ,position = (x,0,0))

for x in range (2):
    if x == 0:
        b = Entity(model="cube",color =  rgb(70,42,42) ,position = (x+2,1,0))
        b = Entity(model="cube",color =  rgb(220,118,51) ,position = (x+3,1,0))
    if x == 1:
        b = Entity(model="cube",color = rgb(70,42,42) ,position = (x+4,1,0))
        b = Entity(model="cube",color =  rgb(220,118,51) ,position = (x+3,1,0))

#rostro medio
for y in range(1,5):
    b = Entity(model="cube",color = rgb(220,118,51) ,position = (0,y,0))

for y in range(1,4):
    b = Entity(model="cube",color = rgb(220,118,51) ,position = (1,y,0))

for y in range(1,5):
    b = Entity(model="cube",color = rgb(220,118,51),position = (7,y,0))

for y in range(1,4):
    b = Entity(model="cube",color = rgb(220,118,51),position = (6,y,0))
for x in range(1,7):
    b = Entity(model="cube",color = rgb(220,118,51),position = (x,5,0))
    b = Entity(model="cube",color = rgb(220,118,51),position = (x,4,0))

for x in range (2,6):
    b = Entity(model="cube",color = rgb(220,118,51),position = (x,2,0))
for x in range(3,5):
    b = Entity(model="cube",color = rgb(220,118,51),position = (x,3,0)) 

#cabello
for x in range(8):
    b = Entity(model="cube",color = rgb(70,42,42),position = (x,6,0)) 
    b = Entity(model="cube",color = rgb(70,42,42),position = (x,7,0)) 
for x in range(0,8,7):
    b = Entity(model="cube",color = rgb(70,42,42),position = (x,5,0)) 

#OJOS
b = Entity(model="cube",color = color.white ,position = (1,3,0))
b = Entity(model="cube",color = color.black ,position = (2,3,0))
b = Entity(model="cube",color = color.black ,position = (5,3,0))
b = Entity(model="cube",color = color.white ,position = (6,3,0))

EditorCamera()
app.run()