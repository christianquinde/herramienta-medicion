#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 10:03:08 2022

@author: paul
"""

import numpy as np
#import pandas as pd
import statistics as stats
import os
import matplotlib.pyplot as plt
from datetime import datetime
import sys


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

        arch = "piso"+piso+"_tx"+tx+".txt"
        file= open(arch,"r")
        datos = file.readlines()
        
        str_match = [s for s in datos if s.__contains__("Fraction lost:")]
        num_fract=len(str_match)
        
        enviados = 256*num_fract
        
        str_acum = [s for s in datos if s.__contains__("Cumulative number of packets lost")]
        tam=len(str_acum)-1
        final=str_acum[tam]
        final2=final.split(":")
        
        perdidos=int(final2[1])
        
        porc=round((100*perdidos)/enviados,4)
        
        media.append(porc)
        
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

plt.ylabel('Packet loss [%]', fontsize=14)
plt.xlabel('Piso', fontsize=14)
plt.xticks(fontsize=13)
plt.yticks(fontsize=13)

if direc=='tx/fraction_loss':
    os.chdir("../../comparacion/fraction_loss")
else:
    os.chdir("../../comparacion/fraction_loss_audio")

plt.savefig("comparacion"+".png")

