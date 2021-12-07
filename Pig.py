from ursina import*

app = Ursina()

#cabeza del cerdo
for x in range(2):
    for y in range(0,8):
        if y == 4:
            h = 0
        else:
            b = Entity(model="cube",color = rgb(255,150,180) ,position = (x,y,0))
            b = Entity(model="cube",color = rgb(255,150,180) ,position = (x+6,y,0))

for x in range(2,6):
    for y in range(4,8):
        b = Entity(model="cube",color = rgb(255,150,180) ,position = (x,y,0))
    b = Entity(model="cube",color = rgb(255,150,180) ,position = (x,0,0))            

#OJOS
for x in range (2):
    if x == 1:
        b = Entity(model="cube",color = color.black ,position = (x+6,4,0))
    else:
         b = Entity(model="cube",color = color.black ,position = (x,4,0))

for x in range (2):
    if x == 1:
        b = Entity(model="cube",color = color.white ,position = (x+5,4,0))
    else:
        b = Entity(model="cube",color = color.white ,position = (x+1,4,0))

#orificio nariz
for x in range (2):
    if x == 1:
        b = Entity(model="cube",color = rgb(100, 30, 1) ,position = (x+4,2,0))
    else:
        b = Entity(model="cube",color = rgb(100, 30, 1) ,position = (x+2,2,0))
#NARIZ
for x in range(2,6):
    b = Entity(model="cube",color = rgb(255,100,150) ,position = (x,3,0))
    b = Entity(model="cube",color = rgb(255,100,150) ,position = (x,1,0))
#medio nariz
for x in range(2):
    if x == 1:
        b = Entity(model="cube",color = rgb(255,100,100) ,position = (x+3,2,0))
    else:
        b = Entity(model="cube",color = rgb(255,100,100) ,position = (x+3,2,0))
EditorCamera()
app.run()
