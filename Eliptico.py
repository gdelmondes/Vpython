from visual import *

a2 = 0.0
vermelho = (255,0,0)
bola = sphere(radius = 0.3, pos = (0, 0, 3.4),
            color = vermelho, make_trail = True)

while True:
    rate(100)
    bola.pos = (3.4) * vector(0,sin(a2), sin(a2) - cos(a2))
    a2 += 0.055
    
