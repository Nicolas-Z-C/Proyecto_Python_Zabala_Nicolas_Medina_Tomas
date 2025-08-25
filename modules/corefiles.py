import os
import time
import random
import modules.json as js 
import modules.menufiles as mn
#Inicio de las funciones de la aplicacion

def clr(): 
 # Limpia la consola dependiendo del sistema operativo
 os.system('cls' if os.name == 'nt' else 'clear') 

def Wait(S:int):
 # Espera S segundos
 time.sleep(S)

def Oprimir():
 # Funcion para cuando hay un error con el usuario
 input("Oprima una tecla para continuar")

def AgregarTrainer():
 print("""
        ---------------------------------------------------------
        |A continuacion porfavor ingrese los datos del Trainer
        ---------------------------------------------------------
        """)
 TrainerNuevo = {
     
     "Nombre":Nombre(),
     "CC":CC(),
     "Direccion":Direccion(),
     "Telefono":Telefono(), 
     }
    
 Trainer={TrainerNuevo["CC"]:TrainerNuevo}
 js.UpdateJson(js.JSON_CUENTAS,Trainer,["TRAINERS"])
 
def CrearCuenta():
 # Esta funcion permite crear una cuenta de usuario sea trainer o camper
 cuenta={}
 while True:
    db=js.ReadJson(js.JSON_CUENTAS)
    print("""
        ---------------------------------------------------------
        |A continuacion porfavor ingrese los datos de los campers
        ---------------------------------------------------------
        """)
    cuentaNueva = {
     
     "Nombre":Nombre(),
     "CC":CC(),
     "Direccion":Direccion(),
     "Acudiente":Acudiente(),
     "Telefono":Telefono(), 
     "Estatus":Estatus(),
     "Riesgo":Riesgo(),
     "Ruta": None
     }
    
    cuenta={cuentaNueva["CC"]:cuentaNueva}
    js.UpdateJson(js.JSON_CUENTAS,cuenta,["CAMPERS"])
    print("Cuenta creada exitosamente")
    print(cuentaNueva)

    op = input("Desea crear otra cuenta? (S/N): ").strip().upper()
    if op == "N":
        return
    elif op == "S":
        continue
    else:
        print("Opcion no valida, porfavor intente de nuevo")
        Oprimir()

def Nombre():
 # Esta funcion permite ingresar el nombre del usuario
 while True:
    clr()
    Nombre=str(input("Porfavor ingrese el nombre seguido del primer apellido del camper: "))
    if Nombre.isalpha() and len(Nombre) > 5:
     return Nombre 
    else:
     print("El nombre y apellido esta mal creado, porfavor revisa tu sintaxis")
     Oprimir()
   

def CC():
 # Esta funcion permite ingresar el numero de cedula del usuario
 while True:
  cuentas=js.ReadJson(js.JSON_CUENTAS)
  clr()
  try:
   cc=int(input("Porfavor ingrese su numero de cedula"))
   if cc in cuentas:
    print("El valor registrado ya se encuentra en nuestra base de datos")
    Oprimir()
   else:
    return cc
  except ValueError:
   print("Valor no soportado")
   Oprimir()

def Direccion():
 # Esta funcion permite ingresar la direccion del usuario
 while True:
  clr()
  dir=str(input("Porfavor ingresa la direccion de residencia del camper"))
  return dir

def Acudiente():
 # Esta funcion permite ingresar el nombre del acudiente del usuario
 while True:
  clr()
  NomAcu=str(input("Porfavor ingrese el nombre del acudiente del camper: "))
  if NomAcu.isdigit:
   print("Valor no soportado, el nombre no puede contener numeros")
   Oprimir()
  else:
   return NomAcu

def Telefono():
 # Esta funcion permite ingresar el telefono del usuario
 while True:
    clr()
    op = input("""
    --------------------------------------------------------------------
    | Ingrese porfavor el tipo de telefono que se registrara al camper |
    |                                                                  |
    | 1. Movil                                                         |
    | 2. Fijo                                                          |
    |                                                                  |
    --------------------------------------------------------------------        
    """)
    match op: 
     case "1":
      try:
        numero=str(input("Digite el telefono movil del camper: "))
        if len(numero) != 10:
         Oprimir()
        else: 
         return numero
      except:
       Oprimir()
     case "2":
      try:
        numero=str(input("Digite el telefono fijo del camper: "))
        if len(numero) != 8 :
         Oprimir()
        else: 
         return numero
      except:
       Oprimir() 
     case _:
      Oprimir()
 
 

def Estatus():
 # Esta funcion permite ingresar el estatus del usuario
 return "Inscrito"
 

def EditarEstatus():
 # Esta funcion permite editar el estatus de un camper
 db = js.ReadJson(js)
 while True:
   cc=str(input("Por favor ingrese la CC del estudiante que desea editar"))
   if cc in db: 
      status=str(input("Ahora ingrese el nuevo estatus del estudiante"))
      db[cc]["Estatus"] == status
      return
   else:
      print("La cedula ingresada no se encuentra registrada")
      Oprimir()

def Riesgo():
 # Esta funcion permite ingresar el nivel de riesgo inicial del usuario
 return "Bajo"
 

def EditarRiesgo(cc: str):
 # Esta funcion permite editar el nivel de riesgo del usuario
 dbNotas = js.ReadJson(js.JSON_NOTAS)
 db = js.ReadJson(js.JSON_CUENTAS)
 for i in dbNotas[cc]["Ruta"]["Modulos"]:
   if len(dbNotas[cc["Ruta"]]) > 1:
      nota = dbNotas[cc]["Ruta"]["Modulos"]
      if nota < 60:
        db[cc]["Riesgo"] = "Alto"
        return
      else:
        pass
   else:
     nota += dbNotas[cc]["Ruta"]["Modulos"]["Total"]
     modulos +=1
 promedio= nota/modulos
 if promedio < 60:
   db[cc]["Riesgo"] = "Alto"
   return

def Rutainicial():
  dbRutas=js.ReadJson(js.JSON_RUTAS)
  rutas= dbRutas.keys()
  ruta=str(input(f"""
-----------------------------------
Las rutas disponibles son: 
{rutas}
Elija una de estas porfavor:
-----------------------------------
"""))
  
def Login():
 # Esta funcion permite iniciar sesion en la aplicacion
   contador = -1
   db=js.ReadJson(js.JSON_CUENTAS)
   while True:
      if len(db) == -1:
         contador += 1
         
      print("""
            ----------------------------------------
            |        Bienvenido Coordinador        |
            ----------------------------------------
            """)
      if contador != 0:
         ContraseñaRegistrada =   input('Ingrese la contraseña del sistema: ')
         if db["contraseñaadmin"] == ContraseñaRegistrada: 
            pass
         else:
            print("Contraseña incorrecta")
            Oprimir()
      else:
         ContraseñaRegistrada = input('Registre la contraseña del sistema.\n Contraseña:  ')
         js.UpdateJson(js.JSON_CUENTAS, {"contraseñaadmin":ContraseñaRegistrada})
         break

def CambiarNota():
 # Esta funcion permite cambiar la nota del Camper
 pass

def VerNotas():
 # Esta funcion permite ver las notas del Camper
 pass

def VerUsuarios():
 # Esta funcion permite ver los usuarios registrados en la aplicacion
 pass   

def CambiarEstatus():
 # Esta funcion permite cambiar el estatus del Camper
 pass   
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
   NotaTotal = (NotaPractica + NotaTeoria + NotaTrabajos) / 3
   NotaTotal = f"{NotaTotal:.1f}"
   return NotaTotal
def TipoNota(modulo):
   Notas = js.ReadJson(js.JSON_NOTAS)
   while True:
      mn.MenuTipoNota()
      try:
         opcion = int(input('Ingrese la opcion que desee\nOpcion: '))
         match opcion:
            case 1:
               NotaAsignada = NotaTeoria()
               Notas[CC][modulo] = NotaAsignada
            case 2:  
               NotaAsignada = NotaPractica()
               Notas[CC][modulo] = NotaAsignada
            case 3:
               NotaAsignada = NotaTrabajos()
               Notas[CC][modulo] = NotaAsignada
            case _:
               print('Opcion no disponible..')
               Oprimir()
      except ValueError:
         print('Error: Solo se pueden ingresar numeros..')
         Oprimir()
def TipoModulo():
   while True:
      try:
         mn.Modulos()
         opcion = int(input('Ingrese la opcion que desee\nOpcion: '))
         match opcion:
            case 1:
               modulo = "MODULO 1"
               TipoNota(modulo)
            case 2:
               modulo = "MODULO 2"
               TipoNota(modulo)
            case 3:
               modulo = "MODULO 3"
               TipoNota(modulo)
            case 4:
               modulo = "MODULO 4"
               TipoNota(modulo)
            case 5:
               modulo = "MODULO 5"
               TipoNota(modulo)
            case _:
               print('La opcion ingresada no esta disponible.')
               Oprimir()
      except ValueError:
         print('Error: Solo se pueden ingresar numeros..')
         Oprimir()
def OrdenRegistroNotas(CC: str):
   notas = {
      CC: {
         "MODULOS": {
            "MODULOS 1": "FUNDAMENTOS DE LA PROGRAMACION",
               "NOTAS": {
                     "TRABAJOS": 0,
                     "PRACTICA": 0,
                     "TEORIA": 0,
                     "TOTAL": 0.0
               },
            "MODULO 2" : "PROGRAMACION WEB",
               "NOTA":{
                     "TRABAJOS": 0,
                     "PRACTICA": 0,
                     "TEORIA": 0,
                     "TOTAL": 0.0                           
            },
            "MODULO 3" : "PROGRAMACION FORMAL",
               "NOTA":{
                     "TRABAJOS": 0,
                     "PRACTICA": 0,
                     "TEORIA": 0,
                     "TOTAL": 0.0                           
            },
            "MODULO 4" : "BASE DE DATOS",
               "NOTA":{
                     "TRABAJOS": 0,
                     "PRACTICA": 0,
                     "TEORIA": 0,
                     "TOTAL": 0.0                           
            },
            "MODULO 5" : "back-end",
               "NOTA":{
                     "TRABAJOS": 0,
                     "PRACTICA": 0,
                     "TEORIA": 0,
                     "TOTAL": 0.0                           
            },
         }
      }
   }
   
   js.InitJson(js.JSON_NOTAS, notas)
pass
def RegistrarNotas():
   db=js.ReadJson(js.JSON_CUENTAS)
   OrdenRegistroNotas()
   while True:
      IdCamper = random.randint(1000, 9999)
      try:
         Camper = input('Ingrese el documento del camper')
         if Camper in db:
            TipoModulo()
         else:
            print('Camper no encontrado..')
            Oprimir()
      except ValueError:
         print('Error')
def InitializeRutas():
   pass
def NuevaRuta():
  # Esta funcion permite crear una nueva ruta
  while True:
   clr() 
   print("Para crear una nueva ruta porfavor ingrese los siguientes datos: ")
   Oprimir()
   dbRutas = js.ReadJson(js.JSON_RUTAS)
   if len(dbRutas) == 12:
      print("Lo sentimos, no puede crear mas rutas, el maximo actual son 12")
      Oprimir()
      return
   else:
      resultadoFunc=SalaEntrenamientoYHorario()
      salon= resultadoFunc(0)
      horario= resultadoFunc(1)
      Ruta = {
      NomRuta():{
         "MODULOS":{Modulos()},
         "SALON":salon,
         "HORARIO":horario,
         "TRAINER":TrainerEncargado(),
         "CAMPERS":{}
      }    
      }
      js.UpdateJson(js.JSON_RUTAS, Ruta)
      op = input("Desea crear otra ruta? (S/N): ").strip().upper()
      if op == "N":
         return
      elif op == "S":
         continue
      else:
         print("Opcion no valida, porfavor intente de nuevo")
         Oprimir()

def Modulos():
  modulosDicc= {
       "Modulos": {
                  "MODULO1":"Fundamentos la programacion",
                  "MODULO2":"Progrmacion Web",
                  "MODULO3":"Programacion Formal",
                  "MODULO4":"Bases de datos",
                  "modulo 5":"Back-end"
                  }
  }
  return modulosDicc

def NomRuta():
 while True:
   clr()
   dbRutas = js.ReadJson(js.JSON_RUTAS)
   NomRuta = str(input("Porfavor ingrese el nombre de la ruta que desea crear"))
   if NomRuta in dbRutas:
      print("Porfavor eliga otro nombre para la ruta este ya se encuentra asignado")
      Oprimir()
   else:
      return NomRuta 

def SalaEntrenamientoYHorario():
  while True:
    clr()
    dbRutas=js.ReadJson(js.JSON_RUTAS)
    salon=str(input("Porfavor escriba el nombre del salon al que desea asignar la ruta(W1,W2,W3)")).upper().strip()
    horario=int(input("Ahora porfavor ingrese el horario al cual desea asignar a la ruta (1|2|3|4)"))
    if horario <= 4:
      for i, x in dbRutas.items():
          if salon == x["SALON"] and horario == x["HORARIO"]:
            print(f"Lo sentimos este salon y horario ya se encuentra reservado para la ruta {i}")
          else:
            salaYHorario=[salon,horario]
            return salaYHorario
def TrainerEncargado():
  while True:
    clr()
    dbCuentas=js.ReadJson(js.JSON_CUENTAS)
    trainer=str(input("Porfavor ingrese el numero de identifiacion del trainer encargado"))
    if trainer in dbCuentas["Trainers"]:
      print("Trainer agregado correctamente")
      Oprimir()
      return trainer
    else:
      print("El trainer mencionado no se encuentra en nuestra base de datos")

def VerRutas():
 clr()
 # Esta funcion permite ver las rutas creadas
 dbRutas= js.ReadJson(js.JSON_RUTAS)
 Rutas= dbRutas.keys()
 print("Las rutas creadas son las siguientes:")
 for i, f in Rutas:
   print(f"""
         -------------------------
         | {i}-{f}
         -------------------------
""")
 pass

def AgregarRuta():
   pass
def BorrarRuta():
 # Esta funcion permite borrar una ruta
 pass    

def EliminarDeRuta():
 # Esta funcion permite eliminar un camper de una ruta
 pass

def CampersInscritos():
 # Esta funcion permite ver los campers inscritos 
 pass

def CampersAprobados():
 # Esta funcion permite ver los campers aprobados
 pass

def Trainers():
 # Esta funcion permite ver los trainers registrados
 pass

def CampersBajoRendimiento():
 # Esta funcion permite ver los campers con bajo rendimiento
 pass  

def CampersYTrainersMismaRuta():
 # Esta funcion permite ver los campers y trainers que estan en la misma ruta
 pass

def Estadisticas():
 # Esta funcion permite ver las estadisticas academicas
 pass


