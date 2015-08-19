#!/usr/bin/python
#*-* coding:utf-8 *-*
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
	os.system("xterm -T free_pops_1.0 -geometry 85x27 +cm -bg blue -e 'sh bin/firmware/a_carga.sh' &")
	time.sleep(8)

    def limpiar(self):
	os.system("rm bin/firmware/a_carga.sh bin/firmware/puerto.txt")

    
    def __init__(self):
	self.b_Puerto()
	self.c_arch_Carga()
	self.limpiar()

if __name__ == "__main__":
    Firmware()
