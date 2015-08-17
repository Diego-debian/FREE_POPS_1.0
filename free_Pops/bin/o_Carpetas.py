#!/usr/bin/python
# -*- coding:utf-8 -*-
#Creado por Diego Alberto Parra Garzón
#Bogotá - Colombia 
import os
import time 
import shutil
import Gnuplot

class App:

    def Carpeta(self):
        self.Carpeta = str(time.asctime())
        os.mkdir(self.Carpeta)

    def c_Carpeta(self):
	archi = open("datos/name.dat","w")
	archi.write(self.Carpeta)
	archi.close()
	time.sleep(3)
        shutil.move("datos/datos_1.dat",  self.Carpeta)
        shutil.move("datos/datos_2.dat",  self.Carpeta)
        shutil.move("datos/datos_3.dat",  self.Carpeta)
        shutil.move("datos/Graf.png",  self.Carpeta)
        shutil.move("datos/Graficas.png",  self.Carpeta)
	os.system("sh bin/m_Carpeta.sh")
  
    def __init__(self):
	self.Carpeta()
	self.c_Carpeta()
	self.__del__()

    def __del__(self):	
        print ("PROGRAMA TERMINADO")
 
 
if __name__ == "__main__":
    App()
