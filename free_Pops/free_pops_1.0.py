#!/usr/bin/python
# *-* coding:utf-8 *-*
#Universidad Distrital Francisco Jose  
#Grupo de fisica e informatica
#Dr Julain Andres Salamanca Bernal
#Diego Alberto Parra Garzón 
#Colombia, Bogota D.C.
#Este programa cuenta con licencia gpl2
import numpy as np
import pylab as pl
import serial
import os
import subprocess
import math
import time
import Gnuplot
from Tkinter import *
import tkMessageBox
import Tkinter
import shutil

class App:
    def Pendulo(self):
        bicho = Tk()
        bicho.geometry("610x430+180+60")
        bicho.config(bg="white")
        bicho.title("free_pops_1.0")
        bicho.resizable(width=0, height=0)
           
        def Salir():
	    tkMessageBox.showinfo("free_pops_1.0", message= "! Cerrando el programa ¡")
	    os.system("rm MAC.txt MACD.txt puerto.txt")

            exit()

        def Verifica():
            try:
                arduino = serial.Serial("/dev/rfcomm0", 9600)
                tkMessageBox.showinfo("free_pops_1.0", message= "! Conectando con el dispositivo, por favor espere ¡")
		time.sleep(2)
    	      #  lblMenu = Label(bicho, text= " Dispositivo listo", fg = ("red"), font = ("Century Schoolbook L",10)).place(x=370, y=100)
                arduino.write("bb")
                Valido()
		
		
                #time.sleep(1)
                
            except:
                tkMessageBox.showinfo("free_pops_1.0", message= "! Dispositivo desconectado ¡")
                os.system("sh c_Blu.sh &")
		#Valido()
                arduino = serial.Serial("/dev/rfcomm0", 9600)
		arduino.close()  
		time.sleep(6)
                os.system("sh c_Blu.sh &")
		#Valido()
                arduino = serial.Serial("/dev/rfcomm0", 9600)
		arduino.close()  
		time.sleep(6)
		
        
        def Valido():
# ................. Botones menu de inicio ....................................
            tkMessageBox.showinfo("free_pops_1.0", message= "! El dispositivo esta conectado ¡")
	    x1 = int(100)
            lblRapidez = Label(bicho, text="\nMENU\nDE INICIO", fg = ("black"), bg = ("white"), font = ("Century Schoolbook L",10)).place(x=15+x1, y=257)
            btnComenzar = Button(bicho, text= "Comenzar", width=5, height=1, command= Comenzar).place(x=20+x1, y=320)
            btnDetener= Button(bicho, text= "Detener", width=5, height=1, command= Boton).place(x=20+x1, y=350)
            btnLimpiar = Button(bicho, text= "limpiar", width=5, height=1, command= Reset).place(x=20+x1, y=380) 	

       
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ Crear carpeta de los datos segun su fecha y hora @@@@@@@@@@@@@@@@@@@@@
        def Carpetas():
	    os.system("python prueba.py &")

#------------------------------------- Funcion limpiar pantalla ---------------------------------------------------
        def Reset():
	    tkMessageBox.showinfo("free_pops_1.0", message= "! Limpiando, por favor espere ¡")
	    os.system("python free_pops_1.0.py &")
	    os.system("rm MAC.txt MACD.txt puerto.txt")
	    exit()

#---------------------------------- LLamando a la funcion imagenes del microcontrolador ----------------------------
        def Comenzar():
            tkMessageBox.showinfo("free_pops_1.0", message= "! Procediendo con la captura de datos, tiempo 30 [s] ¡")
	    os.system("xterm -T free_pops_1.0 -geom 50x8+185+100 +cm -bg blue -e python  bin/i_micro.py & ")
#................... Botones analisis de datos .................................
            x2 = int(70)
	    lblAnalizar = Label(bicho, text="\nANALIZAR\n DATOS ", fg = ("black"), bg = ("white"), font = ("Century Schoolbook L",10)).place(x=140+x2, y=256)             
            btnAnalizar = Button(bicho, text= "Analizar", width=5, height=1, command= Analizar).place(x=140+x2, y=320) 	
            btnGraf= Button(bicho, text= "Graficar", width=5, height=1, command= Graficar).place(x=140+x2, y=350) 	
            btnAnimacion= Button(bicho, text= "Animación", width=5, height=1, command= Simular).place(x=140+x2, y=380) 	

#--------------------Definiendo Funcion analizar datos -------------------------------
	def Graficar():
            tkMessageBox.showinfo("free_pops_1.0", message= "! Realizando las graficas ¡")
	    os.system("python 'bin/g_Estadi.py' &")
		
	def Analizar():
            tkMessageBox.showinfo("free_pops_1.0", message= "! Ahora se analizan los datos capturados y se procede a obtener la frecuencia del sistema ¡")
	    os.system("mv Graf.png datos/Graf.png &")
	    i_Estad()
	
	def Simular():
            tkMessageBox.showinfo("free_pops_1.0", message= "! Se procede hacer la simulación ¡")
	    os.system("python bin/pendulo.py &")

#---------------------------------- Bluetooth desconectado ----------------------------
	def Bl_off():
	    tkMessageBox.showinfo("free_pops_1.0", message= "!Bluetooth desconectado¡")
	    os.system("rm MAC.txt MACD.txt puerto.txt")
	    os.system("sh bin/d_Blu.sh &")

	def Boton():
	    tkMessageBox.showinfo("free_pops_1.0", message= "Para detener la visualización de datos, cierre la ventana de datos 'color azul' u oprima el botón reset del Dispositio ")

# ------------------------------ Definiendo Funcion firmware -----------------------------
	
	def Firmware():
	    tkMessageBox.showinfo("free_pops_1.0", message= "Conecte la tarjeta microcontroladora arduino uno, con un microcontrolador listo para su uso.\n\nProcediendo con el instalador del firmware")
	    os.system("python bin/firmware/G_firmware.py &")


	    


#------------------------------ FUNCION ANALISIS DE DATOS Y GRAFICA  -------------------------------------
        def i_Estad():
	    os.system("python bin/estadistica.py &")            
	    time.sleep(3)
	    Fr = np.loadtxt('importantes/frecuencia.dat')	
    	    L = np.loadtxt('importantes/longitud.dat')	
	    W = np.loadtxt('importantes/angular.dat')	
	    T = np.loadtxt('importantes/periodo.dat')	
	    r = -350
	    s = -150
	    lblLbl = Label(bicho, text = "  ANALISIS PENDULO SIMPLE ",  fg = ("black"), bg = ("white"), font = ("Century Schoolbook L",10)).place(x=400 + r, y=170 + s)
    	    lblFr = Label(bicho, text= " Frecuencia [Hz] :" ,  fg = ("black"),  bg = ("white"), font = ("Century Schoolbook L",10)).place(x=380 + r, y=210 + s)
    	    lblAng = Label(bicho, text= " F. ángular [rad/s] : " ,  fg = ("black"),  bg = ("white"), font = ("Century Schoolbook L",10)).place(x=380 + r, y=250 + s)
    	    lblLon = Label(bicho, text= " Longitud [m] :" ,  fg = ("black"),  bg = ("white"), font = ("Century Schoolbook L",10)).place(x=380 + r, y=290 + s)
    	    lblPer = Label(bicho, text= " Periodo [s] :" ,  fg = ("black"),  bg = ("white"),  font = ("Century Schoolbook L",10)).place(x=380 + r, y=330 + s)
            lblFrecuencia = Label(bicho, text= Fr ,  fg = ("black"),  bg = ("white"), font = ("Century Schoolbook L",10)).place(x=550 + r , y=210 + s)
    	    lblAngular = Label(bicho, text= W,  fg = ("black"),  bg = ("white"), font = ("Century Schoolbook L",10)).place(x=550 + r, y=250 + s)
    	    lblLongitud = Label(bicho, text= L,  fg = ("black"),  bg = ("white"), font = ("Century Schoolbook L",10)).place(x=550 + r , y=290 + s)
   	    lblPeriodo = Label(bicho, text= T ,  fg = ("black"),  bg = ("white"), font = ("Century Schoolbook L",10)).place(x=550 + r , y=330 + s)
	 
#---------------------- Botones Presentacion -----------------------------------------------------------    	
	yn = int(-210)
	imgBoton2=PhotoImage(file="Imagenes/cap8.gif")
        btnLogo= Label(bicho, image=imgBoton2,  height=150, width =180).place(x=400, y=215+yn)
	imgPendulo=PhotoImage(file="Imagenes/pendulo.gif")
        btnPendulo= Label(bicho, image=imgPendulo,  height=146, width =108).place(x=430, y=460+yn)
        lblFisinfor = Label(bicho, text=" Pendulo Simple ", fg = ("black"), bg = ("white"), font = ("Century Schoolbook L",10)).place(x=430, y=610+yn)
        lblFisinfor = Label(bicho, text=" GRUPO DE FISICA E INFORMATICA ", fg = ("black"), bg = ("white"), font = ("Century Schoolbook L",10)).place(x=360, y=371+yn)
	lblInfo = Label(bicho, text="Dr. Julian Andres Salamanca \n Diego Alberto Parra Garzón", fg = ("black"), bg = ("white"), font = ("Century Schoolbook L",10)).place(x=400, y=390+yn)


#---------------------- Botones Bluetooth -----------------------------------------------------------
	y1 = int(32)
        lblBlue = Label(bicho, text="BLUETOOTH ", fg = ("black"), bg = ("white"), font = ("Century Schoolbook L",10)).place(x=10, y=320-y1)
        btnConectar= Button(bicho, text= " ON ", width=5, height=1, command= Verifica).place(x=20, y=350-y1)            
        btnDesconectar= Button(bicho, text= " OFF ", width=5, height=1, command= Bl_off).place(x=20, y=380-y1)  
	btnSalir=Button(bicho, text = "Salir", command=Salir, height=1, width =5).place(x=20, y=410-y1)

#---------------------- Botones firmware -----------------------------------
	btnfirmware=Button(bicho, text = "Firmware", command=Firmware, height=1, width =5).place(x=340, y=380)
        bicho.mainloop()  

   
    def __init__(self):
        self.Pendulo()
        self.__del__()

    def __del__(self):
        print ("PROGRAMA TERMINADO")

if __name__ == "__main__":
    App()

