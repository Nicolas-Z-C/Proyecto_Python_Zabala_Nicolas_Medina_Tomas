"""
dict = { 

    "Ruta":{ 

        "Trainer":"Trainer",
        "modulos":{},
        "salon":"Salon1",
        "horario":"1"
    },

    "Ruta2":{ 

        "Trainer":"Trainer2",
        "modulos":{},
        "salon":"Salon2",
        "horario":"1"
    }
}


sala = "salon"
horaio = "1"


print(len(dict["Ruta2"]))
"""
"""def NotaPractica():
   # Agregrar nota de Practicas
   while True:
      try:
         nota = int(input('Ingrese la nota de las Practicas del Camper\n La nota debe ser de (0 a 100)\n Nota: '))
         if 0 <= nota <= 100:
            print('La nota fue Agregada correctamente.')
            return nota
         else:
            print('La nota solo debe ser de (0 a 100)\nPor favor Ingresar un numero dentro del rango')
            input('oprima para continuar..\n')
      except ValueError:
         print('Error: El dato ingresado solo pueden ser NUMEROS ENTEROS.')
         input('oprima para continuar..\n')

NotaPractica()
diccionario = {'nota':NotaPractica()}
print(diccionario)
"""
def NotaPractica():
   nota = 100
   return nota
def NotaTeoria():
   nota = 20
   return nota
def NotaTrabajos():
   nota = 80
   return nota

NotaPractica = NotaPractica()
NotaTeoria = NotaTeoria()
NotaTrabajos = NotaTrabajos()
NotaTotal = (NotaPractica + NotaTeoria + NotaTrabajos) / 3
NotaTotal = f"{NotaTotal:.1f}"
print(NotaTotal)