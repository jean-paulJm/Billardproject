#!/usr/bin/env python
#-*- coding: utf-8 -*-

def fonc_repartition(Liste):
        for i in range(len(Liste)):
                for j in range(i+1,len(Liste)-1):
                        if round(Liste[i][0],5) == round(Liste[j][0],2) and round(Liste[i][1],2) == round(Liste[j][1],2):
                                return j
        return i
        


from math import *
import numpy as np
import matplotlib.pyplot as plt
angle=float(input("quel angle de référence voulez-vous?: "))
rebond = int(input("Entrez le nombre de rebonds: "))
theta = np.linspace(0, 2*np.pi, 1000)
x=np.cos(theta)+1
y=np.sin(theta)+1
pos=3*pi/2
Graphiquex = [1]
Graphiquey = [0]
Liste=[[pos,angle]]
#------------------------------
for i in range (rebond):
	#pos=((((pos/(2*pi)+angle/pi))%1)*2*pi)%(2*pi)
	pos=(pos+2*angle)%(2*pi)
	posx=cos(pos)+1
	posy=sin(pos)+1
	Graphiquex=Graphiquex+[posx]
	Graphiquey=Graphiquey+[posy]
	Liste=Liste + [[pos,angle]]
#print(Liste)
repartition = fonc_repartition(Liste)
coefficient = float(repartition/rebond)
print ("coefficient de Repartition = ",coefficient)

#------------------------------
#Calcul du cercle circonscrit
Cx=abs(Graphiquex[1]+1)/2
Cy=Graphiquey[1]/2
r=sqrt((Cx-1)**2+(Cy-1)**2)
x2=np.cos(theta)*r+1
y2=np.sin(theta)*r+1


plt.plot(x, y)
plt.plot(x2,y2)
plt.axis("equal")
plt.plot(Graphiquex,Graphiquey, linewidth=0.7)
plt.axis([0.0,2.0,0.0,2.0])
plt.ylabel('')
plt.xlabel('')
plt.show()

