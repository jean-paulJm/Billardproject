#!/usr/bin/env python
#-*- coding: utf-8 -*-
import math
import matplotlib.pyplot as plt
from math import *
mur = ["bas","droit","haut","gauche"]
i = 0 # indice de la liste mur
j = 0 # indice boucle
mur_reference = mur[i]
L=float(input("Entrez la longueur L souhaitée de votre rectangle(axe des abcisses): "))
l=float(input("Entrez la largeur l souhaitée de votre rectangle(axe des ordonnées): "))
angle = float(input("Entrez l'angle de reference (entre 0 et pi): "))
x=-1.0
while x<0.0 or x>L:
    x = float(input("Entrez la coordonnee de reference(entre 0.0 et la longueur L ): "))
rebond = int(input("Entrez le nombre de rebonds: "))
Liste = [[angle,x, mur_reference]]
Graphiquex = [x]
Graphiquey = [i]

for j in range(rebond - 1):
    if i==0 or i==2:
        if x!=L and angle <= atan(l/(L-x)):#or (j==0 and x==0.0 and angle<atan(l/(L-x))): 
            i = (i+1)%4
            x = (L-x)*tan(angle)
            angle = math.pi/2 - angle
        elif x!=L and(atan(l/(L-x)) < angle ) and (angle <= math.pi/2):#or (j==0 and x==0.0 and (atan(l/(L-x)) < angle ) and (angle < math.pi/2)): 
            i = (i+2)%4
            x = L - x - l/tan(angle)
            angle = math.pi - angle #angle alterne-interne
        elif (x!=0.0 and math.pi-atan(l/x) > angle ) and (angle > math.pi/2): 
            i = (i+2)%4
            x = L - x + l/tan(math.pi - angle)
            angle =math.pi - angle #angle alterne-interne
        elif x!=0.0 and angle >= math.pi-atan(l/x) and angle<=math.pi: 
            i = (i+3)%4
            x = l - x*tan(math.pi-angle)
            angle = 3 * math.pi/2 - angle
        else :
            print("error")
    else:
        if x!=l and angle <= atan(L/(l-x)):#or (j==0 and x==0.0 and angle<atan(L/(l-x))): 
            i = (i+1)%4
            x = (l-x)*tan(angle)
            angle = math.pi/2 - angle
        elif x!=l and(atan(L/(l-x)) < angle ) and (angle <= math.pi/2):#or (j==0 and x==0.0 and (atan(L/(l-x)) < angle ) and (angle < math.pi/2)): 
            i = (i+2)%4
            x = l - x - L/tan(angle)
            angle = math.pi - angle #angle alterne-interne
        elif (x!=0.0 and math.pi-atan(L/x) > angle ) and (angle > math.pi/2): 
            i = (i+2)%4
            x = l - x + L/tan(math.pi - angle)
            angle =math.pi - angle #angle alterne-interne
        elif x!=0.0 and angle >= math.pi-atan(L/x) and angle<=math.pi: 
            i = (i+3)%4
            x = L - x*tan(math.pi-angle)
            angle = 3 * math.pi/2 - angle
        else :
            print("error")
    if i == 0:
        graphy = 0
        graphx = x
    elif i == 1:
        graphy = x
        graphx = L
    elif i == 2:
        graphy = l
        graphx = L - x
    elif i == 3:
        graphy = l - x
        graphx = 0
    else:
        print("error")
    Graphiquex = Graphiquex + [graphx]
    Graphiquey = Graphiquey + [graphy]
    mur_reference = mur[i]
    Liste = Liste + [[angle, x, mur_reference]]
    

print(Liste)

plt.title('Trajectoire de la boule dans un rectangle')
plt.plot(Graphiquex,Graphiquey, linewidth=0.7)
plt.axis([0.0,L,0.0,l])
plt.ylabel('')
plt.xlabel('')
plt.show()
