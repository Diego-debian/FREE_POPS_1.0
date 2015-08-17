#!/bin/python
# *-* coding:utf-8 *-*
#Universidad Distrital Francisco Jose  
#Grupo de fisica e informatica
#Dr Julain Andres Salamanca 
#Diego Alberto Parra Garzón 
#Colombia, Bogota D.C.
#Este programa cuenta con licencia gpl2

import numpy as np
import pylab as pl
import os
import subprocess
import math
import time
import shutil
import Gnuplot

gp = Gnuplot.Gnuplot()
gp("set title 'TIEMPO VS VOLTAJE'")
gp("set xlabel 'tiempo [s]'") 
gp("set ylabel 'Voltaje [mV]'")
gp("set yrange auto") 
gp("plot 'datos/datos_1.dat' with lines")
gp("set term png")
gp("set output 'datos/Graf.png'")
gp("replot")
os.system("rm datos/datos_2.dat")
os.system("rm importantes/frecuencia.dat")
os.system("rm importantes/angular.dat")
os.system("rm importantes/periodo.dat")
os.system("rm importantes/longitud.dat")
f = np.loadtxt('datos/datos_1.dat')
x = f[:,0]
y = f[:,1]
#  ...........Asignacion de etiquetas a las variables.................
for i in range (2, 1456):
    a = y[i - 1 ]
    b = y[i]
    c = y[i + 1]
    d = x[i]
    h = float(d)
    g = float(b) 
    g1 = float(a)
    g2 = float (c)
    #  ...........Evaluando las pendientes de la grafica.................
    if a == 0  and b == 0  and  c != 0:
        print "\n", a, "\t", b, "\t", c , " ", i, " ", h
        archi = open ('datos/datos_2.dat','a+')
        xo = str(h)
        yo = str (g)
        archi.write (xo)
        archi.write ("\t ")
        archi.write (yo)
        archi.write("\n")
        archi.close()

    if a != 0 and b == 0 and c == 0:
        print "\n", a, "\t", b, "\t", c , " ", i, " ", h
        archi = open ('datos/datos_3.dat','a+')
        xo = str(h)
        yo = str (g)
        archi.write (xo)
        archi.write ("\t ")
        archi.write (yo)
        archi.write("\n")
        archi.close() 

#--------------------------------- Analizar ----------------------------
f1 = np.loadtxt('datos/datos_2.dat')	
f2 = np.loadtxt('datos/datos_3.dat')	
x4 = f1[:,0]
y5 = f1[:,1]
x5 = f2[:,0]
y6 = f2[:,1]
n_D = int(x4.size)
n_D1 = int(x5.size)
nO = float(n_D/2)
Fr = nO/30
Fr1 = str(round(Fr,3))
T = 1/Fr
T1 = str(round(T,3))
L = 9.81/(Fr*2*np.pi)**2
L1= str(round(L, 3))
l = L*100
W = 2*np.pi*Fr
W1 = str(round(W, 3))
print "\n\n                     ANALISIS PENDULO SIMPLE           \n \n"
print  "| frecuencia [Hz] |    F. ángular [rad/s]  |   Longitud [m]   |   Periodo [s] |" 
print  "|=================|========================|==================|===============|" 
print  "|",Fr," |     ",W,"    | ",L,"  |",T ,"|" 
print  "|=================|========================|==================|===============|" 

#----------------crear archivos importantes-------------
os.system("mkdir importantes")
archi4 = open('importantes/frecuencia.dat', "a+")
archi4.write(Fr1)
archi4.close()

archi5 = open("importantes/angular.dat", "a+")
archi5.write(W1)
archi5.close()

archi6 = open("importantes/longitud.dat", "a+")
archi6.write(L1)
archi6.close()

archi7 = open("importantes/periodo.dat", "a+")
archi7.write(T1)
archi7.close()

exit()
