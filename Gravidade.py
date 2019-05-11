from visual import *
import math

peso = 2
angulo = math.radians(-input("Digite o angulo: "))#Angulo escolhido pelo usuario
g = 9.807 #Gravidade
a = g*math.sin(angulo) #Aceleração
v = 0

rampa = box (pos=[0, 0, 0],
             size=[32, 0.25, 4],
             axis = [angulo,angulo,0],
             color = color.blue)

caixa = box (pos =[(angulo),(angulo)+1+0.25,0],
             size=[2, 2, 2],
             axis = [angulo,angulo,0],
             color = color.red,)

while True:
    rate(3)
    caixa.pos.x += v
    caixa.pos.y += v
    v = a
    if caixa.pos.x < -rampa.size.x/2+5:
        break
