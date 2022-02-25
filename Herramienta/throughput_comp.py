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


direc=sys.argv[1]

eje_x = ['Piso 1', 'Piso 3', 'Piso 5', 'Piso 7']

piso=["1","2","3","4"]
tx=["1","2","3","4","5","6","7","8","9","10"]

#direc = "tx/fraction_loss"
os.chdir(direc)

promc=[]
liminf=[]
limsup=[]
for pi in piso:
    media=[]
    for trans in tx:
        arraygop = []
        ll = []
        arch = "thro_"+"piso"+piso+"_tx"+trans+".csv"
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
        
        prom1 = stats.mean(arraygop)
        media.append(prom1)
        
    prom = stats.mean(media)
    prom=round(prom,2)
    promc.append(prom)
    

    desviacion = np.std(media, 0)
    liminfv = round(prom - 1.96*(desviacion/np.sqrt(len(media))),2)
    liminf.append(liminfv)
    limsupv = round(prom + 1.96*(desviacion/np.sqrt(len(media))),2)
    limsup.append(limsupv)
    
plt.bar(eje_x,promc,color = ["indianred","limegreen","lightseagreen","skyblue"])
for i in range(len(promc)):
    plt.annotate(str(promc[i]), xy=(eje_x[i],promc[i]), ha='center', va='bottom')
    
e=list(np.array(limsup) - np.array(promc))
plt.errorbar(eje_x, promc, yerr=e, fmt='_', ecolor="k",capsize=3)

plt.ylabel('Throughput [kbps]', fontsize=14)
plt.xlabel('Piso', fontsize=14)
plt.xticks(fontsize=13)
plt.yticks(fontsize=13)

if direc=='tx/throughput':
    os.chdir("../../comparacion/throughput")
else:
    os.chdir("../../comparacion/throughput_audio")

plt.savefig("comparacion"+".png")


        


