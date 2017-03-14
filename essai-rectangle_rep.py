#!/usr/bin/env python
#-*- coding: utf-8 -*-

def fonc_repartition(Liste):
        for i in range(len(Liste)):
                for j in range(i+1,len(Liste)-1):
                        if round(Liste[i][0],2) == round(Liste[j][0],2) and round(Liste[i][1],2) == round(Liste[j][1],2):
                                return j
        return i

import numpy as np  
import sys 
import math
import matplotlib.axes as axes
import matplotlib.pyplot as plt 
from math import *
mpl_fig=plt.figure()
ax=mpl_fig.add_subplot(111)
mur = ["bas","droit","haut","gauche"]
i = 0 # indice de la liste mur
j = 0 # indice boucle
mur_reference = mur[i]
L=float(input("Entrez la longueur L souhaitée de votre rectangle(axe des abcisses): "))
l=float(input("Entrez la largeur l souhaitée de votre rectangle(axe des ordonnées): "))
angle = -1
while angle<0.0 or angle>math.pi :
    angle = float(input("Entrez l'angle de reference (entre 0 et pi): "))
x=-1.0
while x<0.0 or x>L:
    x = float(input("Entrez la coordonnee de reference(entre 0.0 et la longueur L ): "))
rebond = int(input("Entrez le nombre de rebonds: "))
Liste = [[angle,x, mur_reference]]
Graphiquex = [x]
Graphiquey = [i]

for j in range(rebond - 1):
    if i==0 or i==2: #Si l'on est sur un des murs du haut ou du bas :
        if x!=L and angle <= atan(l/(L-x)): #Si on va rebondir sur le mur de droite
            i = (i+1)%4
            x = (L-x)*tan(angle)
            angle = math.pi/2 - angle
        elif x!=L and(atan(l/(L-x)) < angle ) and (angle < math.pi/2): #Si on va rebondir sur la partie droite du mur du haut
            i = (i+2)%4
            x = L - x - l/tan(angle)
            angle = math.pi - angle
	elif angle == math.pi/2: #Si on va sur le mur du haut perpendiculairement au mur actuel
	    i = (i+2)%4
	    x = L - x
        elif (x!=0.0 and math.pi-atan(l/x) > angle ) and (angle > math.pi/2): #Si on va rebondir sur la partie gauche du mur du haut
            i = (i+2)%4
            x = L - x + l/tan(math.pi - angle)
            angle =math.pi - angle #angle alterne-interne
        elif x!=0.0 and angle >= math.pi-atan(l/x) and angle<=math.pi: #Si on va rebondir sur le mur de gauche
            i = (i+3)%4
            x = l - x*tan(math.pi-angle)
            angle = 3 * math.pi/2 - angle
        else :
            print("error")
	    sys.exit(1)
    else: #Si l'on est sur un des murs de gauche ou de droite :
        if x!=l and angle <= atan(L/(l-x)): #Voir commentaires du dessus
            i = (i+1)%4
            x = (l-x)*tan(angle)
            angle = math.pi/2 - angle
        elif x!=l and(atan(L/(l-x)) < angle ) and (angle <= math.pi/2):
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
	    sys.exit(1)
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
#print(Liste)    
repartition = fonc_repartition(Liste)
coefficient = float(repartition/rebond)
print ("coefficient de Repartition = ",coefficient)
plt.plot(Graphiquex,Graphiquey, linewidth=0.7)


plt.title('Trajectoire de la boule dans un rectangle')
ax.set_xscale('linear')
ax.set_yscale('linear')
#plt.axis("equal")
plt.axis([0.0,L,0.0,l])
plt.ylabel('')
plt.xlabel('')
plt.show()
