from ursina import *
  
app = Ursina()


#Skin
for x in range(8):
    a = Entity(model="cube",color = rgb(251,211,166) ,position = (x,1,1))

for x in range(8):
    if x != 3 and x != 4:
        a = Entity(model="cube",color = rgb(251,211,166) ,position = (x,2,1))

for x in range(8):
    a = Entity(model="cube",color = rgb(251,211,166) ,position = (x,3,1))

for x in range(8):
    if x != 1 and x != 2 and x != 5 and x != 6:
        a = Entity(model="cube",color = rgb(251,211,166) ,position = (x,4,1))

for x in range(3,7):
    a = Entity(model="cube",color = rgb(251,211,166) ,position = (x,5,1))

for x in range(4,6):
    a = Entity(model="cube",color = rgb(251,211,166) ,position = (x,6,1))

#Mouth

for x in range(3,5):
    a = Entity(model="cube",color = rgb(251,166,248) ,position = (x,2,1))

#Eyes 

a = Entity(model="cube",color = color.white ,position = (1,4,1))
a = Entity(model="cube",color = rgb(0,255,18) ,position = (2,4,1))

a = Entity(model="cube",color = color.white ,position = (6,4,1))
a = Entity(model="cube",color = rgb(0,255,18) ,position = (5,4,1))


#Hair
for x in range(8):
    if x != 3 and x != 4 and x != 5 and x != 6:
        a = Entity(model="cube",color = rgb(255,170,0) ,position = (x,5,1))

for x in range(8):
    if x != 4 and x != 5:
        a = Entity(model="cube",color = rgb(255,170,0) ,position = (x,6,1))

for x in range(8):
    for y in range(2):
        a = Entity(model="cube",color = rgb(255,170,0) ,position = (x,7+y,1))


















EditorCamera()
app.run()

