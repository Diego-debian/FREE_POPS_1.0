#/usr/bin/python
#!*-* coding:utf-8 *-* 
import os 

class App:
    def Presentacion(self):
	os.system("clear")
	print "\t\t  Instalador de FREE_POPS_1.0"    
	print "\n \n \n Bienvenido al software free_pops_1.0, el cual le permitira tener varias horas\n de diversión, entre otras cosas podra crear un circuito que le permitira medir el periodo de oscilación de un pendulo simple, a demas, disfrutara de una interfaz fluida y amigable al usuario. "
	print "\n DESEA CONTINUAR CON LA INSTALACION: \n\t Oprima 1 para si \n\t Oprima 2 para no"
	Pr1 = int(raw_input("Ingrese su respuesta: "))
	if Pr1 == 1:
	    self.Instalar()
	else: 
	    self.exit()

    def Instalar(self):
	os.system("clear")
	print "\n\n ¿Que desea hacer ?\n\n"
	print "\n \t oprima 1 para instalar free_pops_1.0"
	print "\n \t Oprima 2 para desinstalar free_pops_1.0"
	print "\n \t Oprima cualquier tecla para SALIR del instalador\n \n"
	Pr2 = int(raw_input("Ingrese su petición : "))
	if Pr2 == 1:

	    os.system("apt-get update && sudo apt-get upgrade")
	    os.system("apt-get install bluez* gcc g++ emacs gnuplot gnuplot-qt evince octave python-matplotlib python-numpy python-tk python-gnuplot python-serial python-visual* libgtkglextmm* arduino fritzing binutils")
	    print "INSTALACION TERMINADA "
	    print "reinicie su pc"

	elif Pr2 == 2:
	    os.system("apt-get --purge remove emacs gnuplot gnuplot-qt evince octave python-matplotlib python-numpy python-tk python-gnuplot python-serial python-visual* libgtkglextmm* arduino fritzing")
	    os.system("sudo apt-get autoremove")
	    os.system("apt-get update && sudo apt-get upgrade")
	    print " DESINSTALACION EXITOSA "
	    print  "Favor dirijase a la carpeta FREE_POPS_1.0 Y ELIMINELA, DE ESTA MANERA EL PROGRAMA ESTARA ELIMINADO POR COMPLETO"
	    print "Desinstalacion completada ---"
	    print "reinicie su pc"
	    self.exit()

	else:
	    print "cerrando el instalador"
	    self.exit()

    def exit(self):
	exit()
	exit()
	exit()
	  	
    def __init__(self):
	self.Presentacion()
	self.__del__()

    def __del__(self):
	print "FIN DEL PROGRAMA"

if __name__ == "__main__":
    App()
