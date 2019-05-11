from visual import *
import math

angulo = math.radians(-45)
g = 0.5 #Gravidade
a = g*math.sin(angulo)

rampa = box (pos=vector(0, 0, 0),
             size=vector(32, 0.25, 2),
             axis = vector(angulo,angulo,0),
             color = color.green)

c = cylinder (pos =vector(0,1.25,-0.5),
             radius=1,
             axis = vector(0,0,1),
             material= materials.wood)

rotacao = math.radians(180)
sleep(0.5)
for i in range(0,35):
    rate(150)
    c.rotate(angle=rotacao, axis=c.axis, origin=c.pos)
    c.pos.x += a
    c.pos.y += a

