#!/usr/bin/python
# -*- coding:utf-8 -*-
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

import os
import time 
import shutil
import Gnuplot

class o_Carpetas:

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
    o_Carpetas()
