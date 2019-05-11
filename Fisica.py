from visual import *

bola = sphere(pos=vector(0,0.25,0),
              radius = 0.2,
              make_trail = True)

bola2 = sphere(pos=vector(0,0.25,0),
               radius = 0.2,
               make_trail = True,
               color = vector(0,0,255))

bola3 = sphere(pos = vector(0,0.25,0),
               radius = 0.2, make_trail = True
               , color = vector(255,0,0))
bola4 = sphere(pos=(0,0.25,0),radius = 0.2, make_trail=True, color=color.yellow)

campo = box(pos = vector(0,0,0), length = 20,
            height = 0.1, width = 10,
            color = vector(0,255,0))
tam = 10

def traves():
    trave = cylinder(pos = vector(tam,0,1),
                     axis = vector(0,2,0),
                     radius = 0.18)
    
    trave = cylinder(pos = vector(tam,0,-1),
                     axis = vector(0,2,0),
                     radius = 0.18)
    
    travessao = cylinder(pos = vector(tam,2,-1),
                         axis = vector(0,0,2),
                         radius = 0.18)

bola.mass = bola2.mass = bola3.mass = 1.0
bola.p = vector (10, 1, 0.2)
bola2.p = vector (10, 1.8, 0.2)
bola3.p = vector (10, 1, -1.2)
dt = 0.1

def trajetoria(ball, dt):
    for i in range(0,tam):
        rate(15)
        ball.pos += (ball.p/ball.mass)*dt

traves()
trajetoria(bola, dt)
trajetoria(bola2, dt)
trajetoria(bola3, dt)
g=vector(0,-9.8,0)
while bola4.pos.y>=0:
  rate(100)
  g=vector(0,-9.8,-14)
  F=bola4.m*g
  bola4.v=bola4.v+(F/bola4.m)*dt
  bola4.pos=bola4.pos+bola4.v*dt/bola4.m
  t=t+dt
