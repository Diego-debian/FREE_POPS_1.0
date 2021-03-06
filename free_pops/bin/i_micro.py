#!/usr/bin/python
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

import serial
import time
import os
import Gnuplot

class i_micro:
  
    def t_Real(self):
        time.sleep(1)
        os.system ("rm datos/datos_1.dat")
        arduino = serial.Serial("/dev/rfcomm0", '9600')
        time.sleep(1)
        arduino.write("a")
        gp = Gnuplot.Gnuplot()
        gp("set title 'TIEMPO VS VOLTAJE EN EL DIODO LATERAL'")
        gp("set xlabel 'tiempo '") 
        gp("set ylabel 'Voltaje en milivoltios'")
        t0 = float(time.time())
        #un  dato es capturad cada 0.020540972
        for i in range (0 , 1460):
            archi = open('datos/datos_1.dat','a+')
            x = arduino.readline()
            tf = float(time.time())
            tt = tf - t0
	    tts = str(round(tt, 3))
            xo = str(x)
            io = str(tt)
	    print  "\n\n \t\t CAPTURANDO DATOS"
	    print  "\n\n      Tiempo [s] "  , " \t Voltaje [mV]"
            print  "\t", tts , "\t \t   ", xo
            archi.write (tts)
            archi.write (" ")
            archi.write (xo)
            archi.close()
            gp("plot 'datos/datos_1.dat' title ' ' with lines")
        arduino.write("b")	
        exit()
    
  

  # funcion init
    def __init__(self):
        self.t_Real()
        self.__del__()

    def __del__(self):
        print "Fin Programa"

if __name__ == "__main__":
    i_micro()
