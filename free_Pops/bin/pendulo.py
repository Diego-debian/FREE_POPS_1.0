#!/usr/bin/python
#*-* coding:utf-8 *-*
from visual import *
import numpy as np
import math


class App:
    def Display(self):
        l1 = np.loadtxt('importantes/longitud.dat')
        f1 = np.loadtxt('importantes/frecuencia.dat')
        W1 = np.loadtxt('importantes/angular.dat')
        T1 = np.loadtxt('importantes/periodo.dat')
	scene = display()
	scene.title='FREE POPS 1.0'
	scene.autoscale = 0
	self.phi0 = pi * 0.1
	self.phi = self.phi0
	self.m = 1.
	self.g = 9.8
	self.l = l1
	self.dt = 1./50.
	self.f = f1
	self.W = W1
	self.T = T1

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
#	label(pos=(-1,10,0), text='F.angular\n%s[rad/s]' %str(self.W), color =color.yellow)
#	label(pos=(5.5,10,0), text='  Periodo \n %s [s]' %str(self.T), color =color.yellow)

	self.phip= 0

	while self.dt < 30 :
	    self.phipp = -(self.m*self.g*self.l)*self.phi
            self.phip = self.phip + self.phipp*self.dt
            self.phi = self.phi + self.phip*self.dt
	    self.y = self.l - self.l*np.cos(self.phi*self.dt)
	    self.x = self.l*np.sin(self.phi*self.dt)
	    self.vx = -self.W*self.x*np.sin(self.phi*self.dt)
	    self.vy = self.W*self.y*np.cos(self.phi*self.dt)
	    phis = str(round(self.phi, 3))
	    xs = str(round(self.x, 4))
	    ys = str(round(self.y, 6))
	    vxs = str(round(self.vx, 5))
	    vys = str(round(self.vy, 5))
	    #VS = (self.vx**2 + self.vy**2)**(0.5)
            SP.rotate(axis =(0,0,1), angle = self.phip*self.dt)
	    #label(pos=(-7,2,0), text='Posicion en x \n %s [s]' %str(self.x), color =color.yellow)
	    #print "\t    angulo \t   Posición x\t      Posición y\t "
	    print phis , "\t" , xs , "\t" , ys , "\t", vxs , "\t" , vys
    	    rate(50)
    
    def __init__(self):
	self.Display()
	self.Frame()
	self.__del__()

    def __del__(self):
	print "FIN DEL PROGRAMA"

if __name__ == "__main__":
    App()
