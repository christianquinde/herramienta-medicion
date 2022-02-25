# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 09:45:01 2021

@author: Paul Astudillo
"""

import statistics as stats
import os
import sys
import numpy as np
import matplotlib.pyplot as plt


piso=sys.argv[1]
sim =sys.argv[2]
direc=sys.argv[3]


#################################### GStreamer #####################################
#direc = "tx/throughput"
os.chdir(direc)

arraygop = []
ll = []
arch = "thro_"+"piso"+piso+"_tx"+str(sim)+".csv"
file= open(arch)
datos = file.read()
rep = datos.count("bps=",0,len(datos))
inic = 0
p1 = 0
pf = 2
while rep!=inic:
    pos1= datos.find("bps=",p1)
    pos1= pos1+4
    final=datos.find("Time:",pf)
    final= final-1
    thr = datos[pos1:final]
    cam = float(thr)
    cam = cam/1000
    arraygop.append(cam)
    p1 = final+5
    pf = final+5
    inic = inic+1

prom = stats.mean(arraygop)
vec = np.ones(rep)
com2 = vec*1600
vec = vec*prom
x = np.arange(0,rep/10,0.1)
dde = round(prom,2)

plt.plot(x,arraygop,linewidth=0.8)
plt.plot(x,vec,linewidth=0.8)     
plt.ylabel('Throughput [kbps]')
wwq="promedio "+"=" +str(dde)
ll.append(wwq)

com = "umbral red Ad-Hoc = 1600"
ll.append(com)
plt.plot(x,com2,linewidth=0.8,linestyle = 'dashed')
plt.legend(ll,loc="upper right")
os.chdir("..")
os.chdir("..")
if direc=="tx/throughput":
    os.chdir("figuras_throu")
else:
    os.chdir("figuras_throu_audio")
plt.savefig(piso+"_tx"+str(sim)+".png")
#plt.show()
os.chdir("..")

prom = stats.mean(arraygop)
print(str(round(prom,4))) 

