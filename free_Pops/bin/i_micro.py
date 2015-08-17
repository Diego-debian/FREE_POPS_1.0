#!/usr/bin/python
# *-* coding:utf-8 *-*
#Universidad Distrital Francisco Jose  
#Grupo de fisica e informatica
#Dr Julain Andres Salamanca 
#Diego Alberto Parra Garzón 
#Colombia, Bogota D.C.
#Este programa cuenta con licencia gpl2

import serial
import time
import os
import Gnuplot

class App:
  
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
            xo = str(x)
            io = str(tt)
            print  "\t", tt , " \t", x 
            archi.write (io)
            archi.write (" ")
            archi.write (xo)
            archi.close()
            gp("plot 'datos/datos_1.dat' with lines")
        arduino.write("b")	
        exit()
    
  

  # funcion init
    def __init__(self):
        self.t_Real()
        self.__del__()

    def __del__(self):
        print "Fin Programa"

if __name__ == "__main__":
    App()




