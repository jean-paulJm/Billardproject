#!/usr/bin/env python
#-*- coding: utf-8 -*-
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
Liste=[[pos,rebond]]
#------------------------------
for i in range (rebond):
	#pos=((((pos/(2*pi)+angle/pi))%1)*2*pi)%(2*pi)
	pos=(pos+2*angle)%(2*pi)
	posx=cos(pos)+1
	posy=sin(pos)+1
	Graphiquex=Graphiquex+[posx]
	Graphiquey=Graphiquey+[posy]
	#Liste=Liste+
plt.plot(x, y)
plt.plot(Graphiquex,Graphiquey, linewidth=0.7)
plt.axis([0.0,2.0,0.0,2.0])
plt.ylabel('')
plt.xlabel('')
plt.show()

