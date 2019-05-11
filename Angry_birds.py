from visual import *
import math

ang = math.radians(90)
dt=0.07
v0=32
theta = 8*pi/180
g = vector(0,-9.8,0)

bloco1 = box(pos=(2,5,-12), length= 1,
             height = 5, width = 1,
             material= materials.wood, axis=(math.cos(ang),math.sin(ang),0))

bloco2 = box(pos=(0,2,-12), length= 1,
            height = 5, width = 1,
            material= materials.wood)

bloco3 = box(pos=(4,2,-12), length= 1,
            height = 5, width = 1,
            material= materials.wood)

bird = sphere(pos=(0,0,10), radius=1,
              color=color.red, make_trail= True)

bird.m = 0.5
bird.v = vector(0, v0*sin(theta), -(v0*cos(theta)))

pig = sphere(pos=(2,6.5,-12), radius=1, color=color.green)

for i in range(0,100):
    rate(7)
    if bird.pos.z <= bloco2.pos.z:
        bloco2.pos.z -= 1.5
        bloco2.rotate(angle=180, axis=bloco2.axis, origin=bloco2.pos)
        bloco1.pos.y -= 1
        pig.pos.y -= 1
        bloco1.axis.x -= 0.2
        pig.pos.x -= 0.2
        bird.pos.z = bloco2.pos.z
        if bloco1.pos.y < 0:
            bloco1.visible = False
        if pig.pos.y < 0:
            pig.visible = False
        if bloco2.pos.z == -18:
            bird.make_trail = False
            bird.pos.z = bloco2.pos.z
            bloco2.visible = False
            bird.visible = False
    else:
        F = bird.m*g
        bird.v = bird.v+ (F/bird.m)*dt
        bird.pos += bird.v*dt/bird.m
