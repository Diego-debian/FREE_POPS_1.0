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

const int sensor1 = A5;
const int ledRojo = 9;
const int ledVerde = 11;
const int ledAzul = 10;
const int ledEmisor = 2;
long miliVolts1;
long intensidad1;
int brillo1;


void setup()
{
  Serial.begin(9600);
  pinMode(ledAzul, OUTPUT);
  pinMode(ledVerde, OUTPUT);
  pinMode(ledRojo, OUTPUT);
  pinMode(ledEmisor, OUTPUT);
}

void Inten1()  
{
  miliVolts1 = (analogRead(sensor1) *5000L) /1023; //opteniendo el valor sensor
  intensidad1 =miliVolts1;
  brillo1 = map(intensidad1, 0, 5000, 0, 255); //funcion map (mapeo) convierte la variable y le da un rango y un dominio
  brillo1 = constrain(brillo1, 0, 255); //funcion constrain o contenido en el intervalo de analogWrite (0, 255)
  digitalWrite(ledEmisor, HIGH);
  analogWrite(ledAzul, brillo1 );   //Salida del led si esta el obstaculo esta lejos
  analogWrite(ledVerde, 255 - brillo1); //Salida del led si el obstaculo esta cerca
  Serial.print(" "); //salida al Serialporth
  Serial.print(intensidad1);
  Serial.println(" ");
  delay (20);
}
  
void inicio()
{
  digitalWrite(ledRojo, HIGH);   // turn the LED on (HIGH is the voltage level)
  analogWrite(ledAzul, LOW);
  analogWrite(ledVerde, LOW);
  delay(100);               // wait for a second
  digitalWrite(ledRojo, LOW);    // turn the LED off by making the voltage LOW
  analogWrite(ledAzul, HIGH);
  analogWrite(ledVerde, LOW);
  delay(100);
}

void Menu()
{
  
  char opcion = Serial.read();
  switch (opcion )
  {
    case 'a': 
            
              
              while(opcion=='a')
              {
                Inten1();
                Menu();              
              }
              break;
              
      case 'b': 
            
              
              while(opcion=='b')
              {
                inicio();
                Menu();              
              }
              break;
   }
  
}

void loop()
{
  
  inicio();
  Menu();
    
}
