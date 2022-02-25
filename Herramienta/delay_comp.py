#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 21:15:01 2022

@author: paul
"""

import statistics as stats
import os
import matplotlib.pyplot as plt
from datetime import datetime
import sys
import numpy as np

direc=sys.argv[1]

eje_x = ['Piso 1', 'Piso 3', 'Piso 5', 'Piso 7']

piso=["1","2","3","4"]
tx=["1","2","3","4","5","6","7","8","9","10"]
os.chdir(direc)

promc=[]
liminf=[]
limsup=[]
for pi in piso:
    media=[]
    for trans in tx:
        #arch="trafico_tx.txt"
        arch = "piso"+pi+"_tx"+trans+".txt"
        file= open(arch,"r")
        datos = file.readlines()
        
        cabecera = [s for s in datos if s.__contains__("Real-time Transport Control Protocol")]
        
        resp=cabecera[0]
        flag=resp.find("Receiver Report")
        if flag>0:
            cont=0
            for i in range(0,len(datos)):
                enco=datos[i].find("bytes on wire")
                if enco>0:
                    cont=cont+1
                if cont==2:
                    posi=i
                    break
            datos2=datos[posi:len(datos)]
        else:
            datos2=datos
            
        
        delay=[]
        for j in range(0,len(datos2)):
             enco=datos2[j].find("(Receiver Report)")
             if enco>1:
                 revi=datos2[j-75]
                 sen=revi.find("(Sender Report)")
                 if sen>0:
                     frames=datos2[j-119:j+35]
                     A=frames[77]
                     A=A.split()
                     A=A[5]
                     A=A[0:len(A)-4]
                     A = A.replace(".",":")
                     #A=float(A)*1000
                     
                     LSR=frames[2]
                     LSR=LSR.split()
                     LSR=LSR[5]
                     LSR=LSR[0:len(LSR)-4]
                     LSR = LSR.replace(".",":")
                     #LSR=float(LSR)*1000
                     
                     DLSR=frames[136]
                     DLSR=DLSR.split()
                     DLSR=DLSR[6]
                     DLSR=DLSR[1:len(DLSR)]
                     DLSR=float(DLSR)
                     
                     format = '%H:%M:%S:%f'
                     A_LSR=datetime.strptime(A, format)-datetime.strptime(LSR, format)
                     segundos=A_LSR.seconds*1000
                     milisegundos=A_LSR.microseconds/1000
                     
                     suma=segundos+milisegundos
                     
                     call_delay=suma-DLSR
                     call_delay=round(call_delay,4)/2
                     if call_delay>0:
                         delay.append(call_delay)
        
        delay_prom= stats.mean(delay)
        delay_prom=round(delay_prom,4)
        media.append(delay_prom)
        
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

plt.ylabel('Delay [ms]', fontsize=14)
plt.xlabel('Piso', fontsize=14)
plt.xticks(fontsize=13)
plt.yticks(fontsize=13)

if direc=='tx/delay':
    os.chdir("../../comparacion/delay")
else:
    os.chdir("../../comparacion/delay_audio")

plt.savefig("comparacion"+".png")

