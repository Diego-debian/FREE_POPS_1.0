#!/usr/bin/python
# *-* coding:utf-8 *-*
#Universidad Distrital Francisco Jose  
#Grupo de fisica e informatica
#Dr Julain Andres Salamanca 
#Diego Alberto Parra Garzón 
#Colombia, Bogota D.C.
#Este programa cuenta con licencia gpl2

import numpy as np
import matplotlib.pylab as pl
import os
import subprocess
import math
import time
import shutil
class App:

    def Cargar(self):
        f = np.loadtxt('datos/datos_1.dat')
        self.x = f[:,0]
        self.y = f[:,1]
        f1 = np.loadtxt('datos/datos_2.dat')	
        f2 = np.loadtxt('datos/datos_3.dat')	
        self.x4 = f1[:,0]
        self.y5 = f1[:,1]
        self.x5 = f2[:,0]
        self.y6 = f2[:,1]
        self.n_D = int(self.x4.size)
        self.n_D1 = int(self.x5.size)
        self.nO = float(self.n_D/2)
        self.Fr = self.nO/30
        self.Fr1 = str(round(self.Fr, 2))
        self.T = 1/self.Fr
        self.T1 = str(self.T)
        self.L = 9.81/(self.Fr*2*np.pi)**2
        self.L1= str(round(self.L ,  2))
        self.l = self.L*100
        self.W = 2*np.pi*self.Fr
        self.W1 = str(self.W)
        print "\n\n                     ANALISIS PENDULO SIMPLE           \n \n"
        print  "| frecuencia [Hz] |    F. ángular [rad/s]  |   Longitud [m]   |   Periodo [s] |" 
        print  "|=================|========================|==================|===============|" 
        print  "|",self.Fr," |     ",self.W,"    | ",self.L,"  |",self.T ,"|" 
        print  "|=================|========================|==================|===============|" 
        
        print self.n_D
        print self.n_D1

    def Graf1(self):
        pl.subplot(221)
        #time.sleep(10)
        pl.plot(self.x,self.y, 'o-')
        pl.title('Tiempo vs Voltaje \n')
        pl.xlabel('Tiempo [s]')
        pl.ylabel('Voltaje [mV]')

    def Graf2(self):
        pl.subplot(222)
        pl.title('Pendientes')
        pl.xlabel('Tiempo [s]')
        pl.ylabel('Voltaje [mV]')
        pl.axis([0, 30, -20, 20])
        pl.text(6, 12, r' frecuencia [Hz]')
        pl.text(11, 8, r' '+ str(self.Fr1) )
        pl.text(6, -8, r'Longitud cuerda [m]')
        pl.text(11, -12, r' '+ str(self.L1) )
        pl.plot(self.x4, self.y5)
        
    def Graf3(self):
        pl.plot(self.x4, self.y5, 'o--')
        pl.subplot(212)
        pl.plot(self.x4, self.y5)
        pl.plot(self.x,self.y, 'o-')
        pl.xlabel('Tiempo [s]')
        pl.ylabel('Voltaje [mV]')
        pl.title('Tiempo vs Voltaje \n')
        pl.legend(loc='upper left')

    def Plotear(self):
        pl.subplots_adjust(right=0.97)
        pl.subplots_adjust(left=0.11)
        pl.subplots_adjust(bottom=0.13)
        pl.subplots_adjust(top=0.87)
        pl.subplots_adjust(wspace=0.40)
        pl.subplots_adjust(hspace=0.60)
        pl.savefig('datos/Graficas.png')
        pl.show()

    def o_Carpetas(self):
	os.system("python bin/o_Carpetas.py &")

    def __del__(self):
        print ("PROGRAMA TERMINADO")

    def __init__(self):
	self.Cargar()
        self.Graf1()
        self.Graf2()
        self.Graf3()
        self.Plotear()
	self.o_Carpetas()
        self.__del__()
if __name__ == "__main__":
    App()

