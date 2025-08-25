import os
import time
import modules.json as js 
import modules.menufiles as mn

def clr(): 
 # Limpia la consola dependiendo del sistema operativo
 os.system('cls' if os.name == 'nt' else 'clear') 

def Wait(S:int):
 # Espera S segundos
 time.sleep(S)

def Oprimir():
 # Funcion para cuando hay un error con el usuario
 input("Oprima una tecla para continuar")

def NotaPractica():
   # Agregrar nota de Practicas
   while True:
      try:
         clr()
         nota = int(input('Ingrese la nota de las Practicas del Camper\nLa nota debe ser de (0 a 100)\nNota: '))
         if 0<= nota <=100:
            print('La nota fue Agregada correctamente.')
            return nota
         else:
            clr()
            print('La nota solo debe ser de (0 a 100)\nPor favor Ingresar un numero dentro del rango')
            Oprimir()
      except ValueError:
         clr()
         print('Error: El dato ingresado solo pueden ser NUMEROS ENTEROS.')
         Oprimir()
         
def NotaTeoria():
   # Agregrar nota de la Teoria del camper
   while True:
      try:
         clr()
         nota = int(input('Ingrese la nota Teorica del Camper\nLa nota debe ser de (0 a 100)\nNota: '))
         if 0<= nota <=100:
            print('La nota fue Agregada correctamente.')
            return nota
         else:
            clr()
            print('La nota solo debe ser de (0 a 100)\nPor favor Ingresar un numero dentro del rango')
            Oprimir()
      except ValueError:
         clr()
         print('Error: El dato ingresado solo pueden ser NUMEROS ENTEROS.')
         Oprimir()
         
def NotaTrabajos():
   # Agregrar nota de los trabajos del camper
   while True:
      try:
         clr()
         nota = int(input('Ingrese la nota del Trabajo del Camper\nLa nota debe ser de (0 a 100)\nNota: '))
         if 0<= nota <=100:
            print('La nota fue Agregada correctamente.')
            return nota
         else:
            clr()
            print('La nota solo debe ser de (0 a 100)\nPor favor Ingresar un numero dentro del rango')
            Oprimir()
      except ValueError:
         clr()
         print('Error: El dato ingresado solo pueden ser NUMEROS ENTEROS.')
         Oprimir()
         
def NotaTotal():
   # hace la ecuacion de la nota total del camper
   NotaPractica = NotaPractica()
   NotaTeoria = NotaTeoria()
   NotaTrabajos = NotaTrabajos()
   NotaTotal = (NotaPractica + NotaTeorica + NotaTrabajos) / 3
   NotaTotal = f"{NotaTotal:.1f}"
   return NotaTotal
def RegistroNotas():
   notas = {}
   js.InitJson(js.JSON_NOTAS, notas)
   notas = {
      "CC": {
         "FSD": {
               "Modulos": {
                  "modulo 1": "A",
                     "Notas": {
                           "Trabajos": NotaTrabajos(),
                           "Practica": NotaPractica(),
                           "Teoria": NotaTeoria(),
                           "Total": NotaTotal(),
                     }
                  },
                  "modulo 2": {
                     "Nombre": "Progrmacion Web",
                     "Notas": {
                           "Trabajos": NotaTrabajos(),
                           "Practica": NotaPractica(),
                           "Teoria": NotaTeoria(),
                           "Total": NotaTotal(),
                     }
                  },
                  "modulo 3": {
                     "Nombre": "Programacion Formal",
                     "Notas": {
                           "Trabajos": NotaTrabajos(),
                           "Practica": NotaPractica(),
                           "Teoria": NotaTeoria(),
                           "Total": NotaTotal(),
                     }
                  },
                  "modulo 4": {
                     "Nombre": "Bases de datos",
                     "Notas": {
                           "Trabajos": NotaTrabajos(),
                           "Practica": NotaPractica(),
                           "Teoria": NotaTeoria(),
                           "Total": NotaTotal(),
                     }
                  },
                  "modulo 5":"Back-end",
                     "Notas": {
                           "Trabajos": NotaTrabajos(),
                           "Practica": NotaPractica(),
                           "Teoria": NotaTeoria(),
                           "Total": NotaTotal(),
                     }
                  }
               }
         }
   js.UpdateJson(js.JSON_NOTAS, notas)