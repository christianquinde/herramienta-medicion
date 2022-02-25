#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 11:35:34 2022

@author: paul
"""

#import numpy as np
#import pandas as pd
import statistics as stats
import os
#import matplotlib.pyplot as plt
from datetime import datetime
import sys


piso=sys.argv[1]
tx =sys.argv[2]
direc=sys.argv[3]

#direc = "tx/fraction_loss"
os.chdir(direc)

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

print(str(porc))

