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

import serial
import os 
import time

class Firmware:
    def b_Puerto(self):
	os.system("ls /dev/ttyACM* > puerto.txt")
	archi=open("puerto.txt","r")
	puerto = archi.readline()
	self.puerto = str(puerto)
	archi.close()
	print self.puerto
	
    def c_arch_Carga(self):
	archi=open("bin/firmware/a_carga.sh", "a+")
	archi.write("#!/bin/bash")
	archi.write("\n")
	archi.write("CARGA=`avrdude -F -V -c arduino -p ATMEGA328P -b 115200 -U flash:w:bin/firmware/free_pops_firmware.hex -P ")
	archi.write(self.puerto)
	archi.write("`")
	archi.write("\n")
	archi.write('echo "$CARGA"')
#	archi.write("\n")
#	archi.write("echo firmware instalado correctamente")
	archi.write("\n")
	archi.write("sleep 10")
	archi.close()
	time.sleep(1)
	os.system("xterm -T free_pops_1.0 -geom 82x27+0+55 +cm -bg blue -e 'sh bin/firmware/a_carga.sh' &")
	time.sleep(8)

    def limpiar(self):
	os.system("rm bin/firmware/a_carga.sh bin/firmware/puerto.txt")

    
    def __init__(self):
	self.b_Puerto()
	self.c_arch_Carga()
	self.limpiar()

if __name__ == "__main__":
    Firmware()
