#!/usr/bin/env python
#-*- coding: utf-8 -*-

#def fonc_repartition(Liste):
#        for i in range(len(Liste)):
#                for j in range(i+1,len(Liste)-1):
#                        if round(Liste[i][0],2) == round(Liste[j][0],2) and round(Liste[i][1],2) == round(Liste[j][1],2):
#                                return j
#        return i
    
import math
import matplotlib.pyplot as plt
from math import *
from numpy import *
mur = ["bas","droit","haut","gauche"]
i = 0 # indice de la liste mur
j = 0 # indice boucle
mur_reference = mur[i]
L=float(input("Entrez la longueur L souhaitée de votre rectangle(axe des abcisses): "))
l=float(input("Entrez la largeur l souhaitée de votre rectangle(axe des ordonnées): "))
long=float(input("De combien voulez-vous diviser le rectangle sur la longueur?: "))
larg=float(input("De combien voulez-vous diviser le rectangle sur la largeur?: "))
n0=float(L/long)    #division de la Longueur L par ce que l'on veut diviser long, il s'agit de la largeur de nos petits rectangles
X=n0
n1=float(l/larg)    #division de la largeur par larg, largeur de nos petits rectangles
Y=n1
angle = float(input("Entrez l'angle de reference (entre 0 et pi): "))
x=-1.0
while x<0.0 or x>L:
    x = float(input("Entrez la coordonnee de reference(entre 0.0 et la longueur L ): "))
rebond = int(input("Entrez le nombre de rebonds: "))
Liste = [[angle,x, mur_reference]]
Graphiquex = [x]
Graphiquey = [i]
x1e=x

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
        if j!=0:    
                coefdir=graphy/(graphx -x)
                xdeb=graphx
                ydeb=graphy
        else:
                coefdir=0.0
        graphy = 0
        graphx = x
        ordor=graphy-(coefdir*graphx)
    elif i == 1:
        if j!=0:    
                coefdir=(graphy-x)/(graphx -L)
                xdeb=graphx
                ydeb=graphy
        else:
                coefdir= (- x)/(x1e - L)
                xdeb=x1e
                ydeb=0
        graphy = x
        graphx = L
        ordor=graphy-(coefdir*graphx)
    elif i == 2:
        if j!=0:
                coefdir=(graphy-l)/(graphx -L+x)
                xdeb=graphx
                ydeb=graphy
        else:
                coefdir=(- l)/(x1e - L + x)
                xdeb=x1e
                ydeb=0
        graphy = l
        graphx = L - x
        ordor=graphy-(coefdir*graphx)
    elif i == 3:
        if j!=0:
                coefdir=(graphy-l+x)/graphx
                xdeb=graphx
                ydeb=graphy
        else:
                coefdir=(- l + x)/(x1e)
                xdeb=x1e
                ydeb=0
        graphy = l - x
        graphx = 0
        ordor=graphy-(coefdir*graphx)
    else:
        print("error")
    Graphiquex = Graphiquex + [graphx]
    Graphiquey = Graphiquey + [graphy]
    mur_reference = mur[i]
    Liste = Liste + [[angle, x, mur_reference]]
    X0=0
    Y0=0
    while X0<xdeb:
            X0+=n0
    while Y0<ydeb:
            Y0+=n1
    while X0<=graphx:
            A=matrix([[coefdir,-1],[1,0]])
            B=matrix([[-ordor],[X0]])
            solution=linalg.solve(A,B)
            X0=X0+n0
            print(solution)
    while Y0<=graphy:
            A=matrix([[coefdir,-1],[0,1]])
            B=matrix([[-ordor],[Y0]])
            solution=linalg.solve(A,B)
            Y0=Y0+n1
            print(solution)
        
print(Liste)    
#repartition = fonc_repartition(Liste)
#coefficient = float(repartition/rebond)
#print ("coefficient de Repartition = ",coefficient)
while X <L:     #affichage des droites verticales , X est la coordonnée des abscisses et va augmenter jusqu'à atteindre la longueur

        plt.plot([X,X],[0,l],'k-',linewidth=0.5)
        X=X+n0

while Y<l:      #affichage des droites horizontales , Y est la coordonnée des ordonnées et va augmenter jusqu'à atteindre la largeur

        plt.plot([0,L],[Y,Y],'k-',linewidth=0.5)
        Y=Y+n1

plt.title('Trajectoire de la boule dans un rectangle')
plt.plot(Graphiquex,Graphiquey, linewidth=0.7)

#plt.axis("equal")
plt.axis([0.0,L,0.0,l])
plt.ylabel('')
plt.xlabel('')
plt.show()
