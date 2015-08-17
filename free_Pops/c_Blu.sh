#!/bin/bash
#/etc/init.d/bluetooth restart
#Universidad Distrital Francisco Jose  
#Grupo de fisica e informatica
#Dr Julain Andres Salamanca 
#Diego Alberto Parra Garzón 
#Colombia, Bogota D.C.
#Este programa cuenta con licencia gpl2
hcitool dev > log.txt | grep -e 'hci0' log.txt > mac.txt
cut -d "0" -f 2,3  mac.txt > MAC.txt
MAC=`cat MAC.txt`
echo "La mac del dispositivo es : $MAC"
hcitool scan > dispo.txt | grep -e "HC-06" dispo.txt > macd.txt
cut -d "H" -f  1  macd.txt > MACD.txt
MACD=`cat MACD.txt`
echo "dispositivo HC-06 encontrado MAC: $MACD"
/etc/init.d/bluetooth restart
rm log.txt mac.txt dispo.txt macd.txt
rfcomm connect 0 $MACD
