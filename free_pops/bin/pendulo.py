#!/usr/bin/python
#*-* coding:utf-8 *-*

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

from visual import *
import numpy as np
import math
import time
import os
import Gnuplot

class pendulo:
    def Display(self):
        l1 = np.loadtxt('importantes/longitud.dat')
        f1 = np.loadtxt('importantes/frecuencia.dat')
        W1 = np.loadtxt('importantes/angular.dat')
        T1 = np.loadtxt('importantes/periodo.dat')
	scene = display()
	scene.title='Pendulo Simple'
	scene.autoscale = 0
	self.phi0 = pi * 0.1
	self.phi = self.phi0
	self.m = 0.050
	self.g = 9.81
	self.l = l1
	self.f = f1
	self.W = W1
	self.T = T1
	self.dt = 0.6/self.T
	

    def Frame(self):
	SP = frame()
	masa = sphere(frame = SP, pos = (0.,-6.9,0.) , radius = 0.7 , color = color.cyan)
	hilo = cylinder(frame =SP, axis= masa.pos, radius = 0.05 , color = color.white)
	soporte = box(pos = (0, 1 , 0), size = (2, 2 , 0.1), color = color.white)
	SP.rotate(axis =(0,0,1), angle =self.phi)
	label(pos=(-7,10,0), text='Frecuencia\n %s [Hz]' %str(self.f), color =color.yellow)
	label(pos=(-7,6,0), text='F. angular\n %s [rad/s]' %str(self.W), color =color.yellow)
	label(pos=(-7,2,0), text='Periodo \n %s [s]' %str(self.T), color =color.yellow)
	label(pos=(-7,-2,0), text='Longitud \n %s [m]' %str(self.l), color =color.yellow)
	self.phip= 0
	self.t0 = float(time.time())
	os.system("rm datos/datos_ttheta.dat")
	os.system("rm datos/datos_txy.dat")
	os.system("rm datos/datos_xvx.dat")
	self.gp = Gnuplot.Gnuplot()
	self.gp1 = Gnuplot.Gnuplot()
	while 1 :
	    self.tf = float(time.time())
	    self.tt = self.tf - self.t0
      	    self.phipp = -(self.m*self.g*self.l)*self.phi
            self.phip = self.phip + self.phipp*self.dt
            self.phi = self.phi + self.phip*self.dt
	    tetha = 180*self.phi*0.26
	    self.phis = str(round(tetha, 3))
	    self.y = 0.5*self.l*cos(tetha)
	    self.x = 0.5*self.l*sin(tetha)
	    self.vx = 0.5*self.W*self.l*cos(tetha)
	    self.vy = -0.5*self.W*self.l*sin(tetha)
	    self.ax = -0.5*self.W*self.W*self.l*sin(tetha)
	    self.ay = -0.5*self.W*self.l*cos(tetha)
	    self.Kx = 0.5*self.m*self.vx**2
	    self.Ux = 0.5*self.l*self.m*self.g*self.x**2
	    self.xs = str(round(self.x, 3))
	    self.ys = str(round(self.y, 3))
	    self.vxs = str(round(self.vx, 3))
	    self.vys = str(round(self.vy, 3))
	    self.axs = str(round(self.ax, 3))
	    self.ays = str(round(self.ay, 3))
	    self.Kxs = str(round(self.Kx, 3))
	    self.Uxs = str(round(self.Ux, 4))
	    self.tt = str(round(self.tt, 4))
	    self.EM = self.Kx + self.Ux
            SP.rotate(axis =(0,0,1), angle = self.phip*self.dt)
	    print self.tt, "\t", self.phis , "	" , self.xs , "	"  , self.vxs , "	",  self.axs , "	",  self.Kxs, "	", self.Uxs, "\t", self.EM, "	\n"	
    	    rate(50)
	    self.Graf1()
	    self.Graf2()
	else:
	    self.gp("exit")	
	    self.gp1("exit")
	    print "Fin del Programa"

    def Graf1(self):
        self.gp("set title 'Variación angular en el tiempo'")
        self.gp("set xlabel 'tiempo [s]'") 
        self.gp("set ylabel 'Posición ángulo [grados]'")
	self.gp("set autoscale")
        archi = open('datos/datos_ttheta.dat','a+')
	archi.write (self.tt)
        archi.write ("\t")
        archi.write (self.phis)
	archi.write("\n")
        archi.close()
        self.gp("plot 'datos/datos_ttheta.dat' title ' ' with lines")
	

    def Graf2 (self):
        self.gp1("set title 'Angulo vs Distancia x vs Distancia y'")
        self.gp1("set xlabel 'Angulo [grados]'") 
        self.gp1("set ylabel 'Distancia x [m]'")
        self.gp1("set zlabel 'Distancia y [m]'")
	self.gp1("set autoscale")
	archi1 = open('datos/datos_txy.dat','a+')
	archi1.write (self.phis)
        archi1.write ("\t")
        archi1.write (self.xs)
	archi1.write("\t")
	archi1.write(self.ys)
	archi1.write("\n")
        archi1.close()
#        self.gp1("splot 'datos/datos_txy.dat' title ' ' with lines")

    def __init__(self):
	self.Display()
	self.Frame()
	self.__del__()

    def __del__(self):
	print "FIN DEL PROGRAMA"

if __name__ == "__main__":
    pendulo()
