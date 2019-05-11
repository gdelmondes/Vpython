from visual import *
#Lissjous3D
a2 = 0.0
vermelho = (255,0,0)
b2 = sphere(radius = 0.3, pos = (0, 0, 3.4),
            color = vermelho, make_trail = True)

while True:
    rate(100)
    b2.pos = (3.4) * vector(sin(4*a2), cos(7*a2))
    a2 += 0.055
    
