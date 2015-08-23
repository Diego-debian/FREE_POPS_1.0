#!/bin/python
# *-* coding:utf-8 *-*
# Este script es sofware libre. Puede redistribuirlo y/o modificarlo bajo 
# los terminos de la licencia pública general de GNU, según es publicada 
# por la free software fundation bien la versión 3 de la misma licencia 
# o de cualquier versión posterior. (según su elección ).
# Si usted hace alguna modificación en esta aplicación, deberá siempre
# mencionar el autor original de la misma.
# Autor: 
# Universidad Distrital Francisco Jose  
# Grupo de fisica e informatica
# Dr Julian Andres Salamanca Bernal
# Diego Alberto Parra Garzón 
# Colombia, Bogota D.C.


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
os.system("rm datos/datos_3.dat")
os.system("rm importantes/frecuencia.dat")
os.system("rm importantes/angular.dat")
os.system("rm importantes/periodo.dat")
os.system("rm importantes/longitud.dat")
#os.system("rm ../datos/datos_2.dat")
#os.system("rm ../datos/datos_3.dat")
#os.system("rm ../importantes/frecuencia.dat")
#os.system("rm ../importantes/angular.dat")
#os.system("rm ../importantes/periodo.dat")
#os.system("rm ../importantes/longitud.dat")#f = np.loadtxt('../datos/datos_1.dat')
#gp("replot")
#f = np.loadtxt('../datos/datos_1.dat')
f = np.loadtxt('datos/datos_1.dat')
x = f[:,0]
y = f[:,1]
#  ...........Asignacion de etiquetas a las variables.................
for i in range (5, 1456):
    a1 = y[i - 5]
    a2 = y[i - 4]
    a3 = y[i - 3 ]
    a4 = y[i - 2 ]
    a5 = y[i - 1 ]
    a6 = y[i]
    b1 = float(a1)   
    b2= float(a2)   
    b3= float(a3)   
    b4= float(a4)   
    b5 = float(a5)   
    b6 = float(a6)   
 
    r = x[i-4]   

    #  ...........Evaluando las pendientes de la grafica.................

    if a1 < a2  and a2 < a3   and  a3 < a4 and  a4 >= a5 :
        print "\n", r, "\t", a4
        archi = open ('datos/datos_2.dat','a+')
#        archi = open ('../datos/datos_2.dat','a+')
        xo = str(r)
        yo = str (a4)
        archi.write (xo)
        archi.write ("\t ")
        archi.write (yo)
        archi.write("\n")
        archi.close()

    if a1 <= a2  and a2 > a3   and  a3 > a4 and  a4 > a5 :
	print "\n", r, "\t", a1
        archi = open ('datos/datos_3.dat','a+')
#        archi = open ('../datos/datos_3.dat','a+')
        xo = str(r)
        yo = str (a1)
        archi.write (xo)
        archi.write ("\t ")
        archi.write (yo)
        archi.write("\n")
        archi.close() 

#--------------------------------- Analisis de las pendientes ----------------------------

#f1 = np.loadtxt('../datos/datos_3.dat')	
#f2 = np.loadtxt('../datos/datos_3.dat')	
f1 = np.loadtxt('datos/datos_2.dat')	
f2 = np.loadtxt('datos/datos_3.dat')	
x1 = f1[:,0]
y1 = f1[:,1]
x2 = f2[:,0]
y2 = f2[:,1]
n_D = int(x1.size)
n_D1 = int(x2.size)
nO = float((n_D + n_D1 )/2)
Fr = (2+nO)/60
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
print  "|   ",Fr1,"\t  | \t    ",W1,"    \t   |  \t",L1," \t      |",T1 ,"\t      |" 
print  "|=================|========================|==================|===============|" 
print n_D

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
