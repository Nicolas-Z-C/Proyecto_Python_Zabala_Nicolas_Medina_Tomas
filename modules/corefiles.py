import os
import time
from datetime import date

import modules.Js as js 

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

def IniciarJsons1():
 estructuraInicialCuentas = {
        "CAMPERS": {},
        "RUTAS": {}
    }
 a = {}
 js.InitJson(js.JSON_NOTAS, a)
 js.InitJson(js.JSON_CUENTAS, estructuraInicialCuentas)
  
def IniciarJsonRutas():
 fechas= FechaFinal()
 fechaInicio=fechas(0)
 fechaFinalizacion=fechas(1)      
 estructuraInicialRutas={
        "NODEJS": {
         "SALON":"W1",
         "HORARIO":1,
         "TRAINER":TrainerEncargado("NODEJS"),
         "CAMPERS":[],
         "FECHAINICIO":fechaInicio,
         "FECHAFINAL": fechaFinalizacion,
         "CAMPERSAPROVADOS": 0,
         "CAMPERSNOAPROVADOS": 0,    
        },
        "JAVA": {
         "SALON":"W2",
         "HORARIO":1,
         "TRAINER":TrainerEncargado("JAVA"),
         "CAMPERS":[],
         "FECHAINICIO":fechaInicio,
         "FECHAFINAL": fechaFinalizacion,
         "CAMPERSAPROVADOS": 0,
         "CAMPERSNOAPROVADOS": 0,    
        },
        "NETCORE": {
         "SALON":"W3",
         "HORARIO":1,
         "TRAINER":TrainerEncargado("NETCORE"),
         "CAMPERS":[],
         "FECHAINICIO":fechaInicio,
         "FECHAFINAL": fechaFinalizacion,
         "CAMPERSAPROVADOS": 0,
         "CAMPERSNOAPROVADOS": 0,  
        },  
    }

 js.InitJson(js.JSON_RUTAS, estructuraInicialRutas)

def AgregarTrainer():
 print("""
        ---------------------------------------------------------
        |A continuacion porfavor ingrese los datos del Trainer
        ---------------------------------------------------------
        """)
 TrainerNuevo = {
     
     "NOMBRE":Nombre(),
     "CC":CC(),
     "DIRECCION":Direccion(),
     "TELEFONO":Telefono(),
     "RUTA": [],
     "ESTADO": "ACTIVO"  
     }
    
 Trainer={TrainerNuevo["CC"]:TrainerNuevo}
 js.UpdateJson(js.JSON_CUENTAS,Trainer,["TRAINERS"])
 
def CrearCuenta():
 # Esta funcion permite crear una cuenta de usuario sea trainer o camper
 cuenta={}
 while True:
    print("""
        __________________________________________________________
        |A continuacion porfavor ingrese los datos de los campers|
        ----------------------------------------------------------
        """)
    cuentaNueva = {
     
     "Nombre":Nombre(),
     "CC":CC(),
     "DIRECCION":Direccion(),
     "ACUDIENTE":Acudiente(),
     "TELEFONO":Telefono(), 
     "ESTATUS":"INSCRITO",
     "RIESGO":"BAJO",
     "RUTA": None
     }
    
    cuenta={cuentaNueva["CC"]:cuentaNueva}
    js.UpdateJson(js.JSON_CUENTAS,cuenta,["CAMPERS"])
    js.UpdateJson(js.JSON_NOTAS,OrdenRegistroNotas(cuentaNueva["CC"]))
    print("Cuenta creada exitosamente")
    print(cuentaNueva)
    try:
      op = input("Desea crear otra cuenta? (S/N): ").strip().upper()
      if op == "N":
         return
      elif op == "S":
         continue
      else:
         print("Opcion Ingresada no disponible.")
         Oprimir()
    except ValueError:
      print('Error: Solo se pueden ingresar letras.')
      Oprimir()

def Nombre():
 # Esta funcion permite ingresar el nombre del usuario
 while True:
   clr()
   try:   
      Nombre=str(input("Porfavor ingrese el nombre seguido del primer apellido del camper: "))
      if not nombre.strip():
       raise ValueError("El nombre no puede estar vacío.")
       Oprimir()
      elif not nombre.replace(" ", "").isalpha():
       raise ValueError("El nombre solo puede contener letras.")
      else:
       return Nombre
   except ValueError as e:
      print(f"Error: {e}. Intente de nuevo.")
      Oprimir()

def CC():
 # Esta funcion permite ingresar el numero de cedula del usuario
 while True:
  cuentas=js.ReadJson(js.JSON_CUENTAS)
  clr()
  try:
   cc=int(input("Porfavor ingrese su numero de cedula: "))
   if not nombre.strip():
      raise ValueError("El Numero de cedula no puede estar vacío.")
      Oprimir()
   elif cc in cuentas:
    print("El valor registrado ya se encuentra en nuestra base de datos")
    Oprimir()
   else:
    return cc
  except ValueError:
   print("Solo se pueden ingresar numeros")
   Oprimir()

def Direccion():
 # Esta funcion permite ingresar la direccion del usuario
 while True:
   clr()
   dire =str(input("Porfavor ingresa la direccion de residencia del camper: "))
   if not nombre.strip():
      raise ValueError("El nombre no puede estar vacío.")
      Oprimir()
   else:
      return dire

def Acudiente():
 # Esta funcion permite ingresar el nombre del acudiente del usuario
 while True:
  clr()
  NomAcu=str(input("Porfavor ingrese el nombre del acudiente del camper: "))
  if not NomAcu:
      print("El nombre no puede estar vacio")
      Oprimir()
      continue
  else:
   return NomAcu

def Telefono():
 # Esta funcion permite ingresar el telefono del usuario
 while True:
    clr()
    try:
      op = int(input("""
      --------------------------------------------------------------------
      | Ingrese porfavor el tipo de telefono que se registrara al camper 
      |                                                                  
      | 1. Movil                                                         
      | 2. Fijo                                                          
      |                                                                  
      --------------------------------------------------------------------        
      : """))
      match op: 
         case 1:
            numero=str(input("Digite el telefono movil del camper: "))
            if len(numero) != 10:
               print('El numeor es invalido.')
               Oprimir()
            else: 
               return numero
         case 2:
            numero=str(input("Digite el telefono fijo del camper: "))
            if len(numero) != 8: 
               print('El numeor es invalido.')
               Oprimir()
            else: 
               return numero
         case _:
            Oprimir()
    except ValueError:
       print('Error: Solo se pueden ingresar numeros.')
       Oprimir()
def EditarEstatus():
 # Esta funcion permite editar el estatus de un camper
 db = js.ReadJson(js.JSON_CUENTAS)
 while True:
   cc=str(input("Por favor ingrese la CC del estudiante que desea editar"))
   if cc in db: 
      status=str(input("Ahora ingrese el nuevo estatus del estudiante"))
      db["CAMPERS"][cc]["Estatus"] == status 
      js.UpdateJson(js.JSON_CUENTAS, db,)
      return 
   else:
      print("La cedula ingresada no se encuentra registrada")
      Oprimir()

def EditarRiesgo(cc: str,ModuloATomar):
 # Esta funcion permite editar el nivel de riesgo del usuario
 dbNotas = js.ReadJson(js.JSON_NOTAS)
 db = js.ReadJson(js.JSON_CUENTAS)
 for i in dbNotas[cc]["Modulos"]:
     nota += dbNotas[cc]["Modulos"][ModuloATomar]["Total"]
     modulos +=1
 promedio= nota/modulos
 if promedio < 60:
   db[cc]["Riesgo"] = "Alto"
   return
  
def Login():
 # Esta funcion permite iniciar sesion en la aplicacion
   contador = -1
   db=js.ReadJson(js.JSON_CUENTAS)
   while True:
      if len(db) == 2:
         contador += 1
         
      print("""
            ----------------------------------------
            |        Bienvenido Coordinador        |
            ----------------------------------------
            """)
      if contador != 0:
         ContraseñaRegistrada =   input('Ingrese la contraseña del sistema: ')
         if db["contrasenaadmin"] == ContraseñaRegistrada: 
            return
         else:
            print("Contraseña incorrecta")
            Oprimir()
      else:
         ContraseñaRegistrada = input('Registre la contraseña del sistema.\n Contraseña:  ')
         js.UpdateJson(js.JSON_CUENTAS, {"contrasenaadmin":ContraseñaRegistrada})
         break
def VerNotas():
 # Esta funcion permite ver las notas del Camper
 dbNotas=js.ReadJson(js.JSON_NOTAS)
 while True:
   try:
      cc=int(input("Ingrese la cedula del camper al que desea mirar las notas: "))
      if cc in dbNotas:
         print(dbNotas[cc])
         Oprimir()
         return
      else:
        print("El camper requerido no se encuentra en nuestra base de datos")
        Oprimir()
        continue
   except ValueError:
     print("Valor no soportado")
     Oprimir()
def VerUsuarios():
 # Esta funcion permite ver los usuarios registrados en la aplicacion
 dbCuentas= js.ReadJson(js.JSON_CUENTAS)
 Cuentas= dbCuentas["CAMPERS"].keys()
 print("Las rutas creadas son las siguientes:")
 for i, f in Cuentas:
   print(f"""
         -------------------------
         | {i}-{f}
         -------------------------
""")
 pass   

def VerTrainer():
 # Esta funcion permite ver los usuarios registrados en la aplicacion
 dbCuentas= js.ReadJson(js.JSON_CUENTAS)
 Cuentas= dbCuentas["TRAINERS"].keys()
 print("Los Trainers son los siguientes:")
 for i, f in Cuentas:
   print(f"""
         -------------------------
         | {i}-{f}
         -------------------------
""")
 pass   

def EditarEstatus():
 # Esta funcion permite editar el estatus de un camper
 db = js.ReadJson(js.JSON_CUENTAS)
 while True:
   cc=str(input("Por favor ingrese la CC del estudiante que desea editar: "))
   if cc in db["CAMPERS"]: 
      status=str(input("Ahora ingrese el nuevo estatus del estudiante(APROVADO|EXPULSADO|CURSANDO): "))
      db["CAMPERS"][cc]["ESTATUS"] = status 
      js.UpdateJson(js.JSON_CUENTAS, db,)
      return 
   else:
      print("La cedula ingresada no se encuentra registrada")
      Oprimir() 
      
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
         
def NotaTotal(modulo, Camper):
   # hace la ecuacion de la nota total del camper
   Notas = js.ReadJson(js.JSON_NOTAS)
   NotaPractica = Notas[Camper]["MODULOS"][modulo]["NOTAS"]["PRACTICA"]
   NotaTeoria = Notas[Camper]["MODULOS"][modulo]["NOTAS"]["TEORIA"]
   NotaTrabajo = Notas[Camper]["MODULOS"][modulo]["NOTAS"]["TRABAJOS"]
   SumaTotal = (NotaTeoria+NotaTrabajo+NotaPractica) / 3
   return SumaTotal

def TipoNota(modulo, Camper):
   Notas = js.ReadJson(js.JSON_NOTAS)
   while True:
      mn.MenuTipoNota()
      try:
         opcion = int(input('Ingrese la opcion que desee\nOpcion: '))
         match opcion:
            case 1:
               NotaAsignada = NotaTeoria()
               Notas[Camper]["MODULOS"][modulo]["NOTAS"]["TEORIA"] = NotaAsignada
            case 2:  
               NotaAsignada = NotaPractica()
               Notas[Camper]["MODULOS"][modulo]["NOTAS"]["PRACTICA"] = NotaAsignada
            case 3:
               NotaAsignada = NotaTrabajos()
               Notas[Camper]["MODULOS"][modulo]["NOTAS"]["TRABAJOS"] = NotaAsignada
            case _:
               print('Opcion no disponible..')
               Oprimir()
      except ValueError:
         print('Error: Solo se pueden ingresar numeros..')
         Oprimir()
        
def TipoModulo(Camper):
   while True:
      try:
         mn.Modulos()
         opcion = int(input('Ingrese la opcion que desee\nOpcion: '))
         match opcion:
            case 1:
               modulo = "MODULO 1"
               TipoNota(modulo, Camper)
               NotaTotal(modulo, Camper)
            case 2:
               modulo = "MODULO 2"
               TipoNota(modulo, Camper)
               NotaTotal(modulo, Camper)
            case 3:
               modulo = "MODULO 3"
               TipoNota(modulo, Camper)
               NotaTotal(modulo, Camper)
            case 4:
               modulo = "MODULO 4"
               TipoNota(modulo, Camper)
               NotaTotal(modulo, Camper)
            case 5:
               modulo = "MODULO 5"
               TipoNota(modulo, Camper)
               NotaTotal(modulo, Camper)
            case _:
               print('La opcion ingresada no esta disponible.')
               Oprimir()
      except ValueError:
         print('Error: Solo se pueden ingresar numeros..')
         Oprimir()
         
def OrdenRegistroNotas(CC: str):
   notas = {
      CC:{
         "MODULOS": {
            "MODULOS 1": "FUNDAMENTOS DE LA PROGRAMACION",
               "NOTAS": {
                     "TRABAJOS": 0,
                     "PRACTICA": 0,
                     "TEORIA": 0,
                     "TOTAL": 0.0
               },
            "MODULO 2" : "PROGRAMACION WEB",
               "NOTAMODULO2":{
                     "TRABAJOS": 0,
                     "PRACTICA": 0,
                     "TEORIA": 0,
                     "TOTAL": 0.0                           
            },
            "MODULO 3" : "PROGRAMACION FORMAL",
               "NOTAMODULO3":{
                     "TRABAJOS": 0,
                     "PRACTICA": 0,
                     "TEORIA": 0,
                     "TOTAL": 0.0                           
            },
            "MODULO 4" : "BASE DE DATOS",
               "NOTAMODULO4":{
                     "TRABAJOS": 0,
                     "PRACTICA": 0,
                     "TEORIA": 0,
                     "TOTAL": 0.0                           
            },
            "MODULO 5" : "back-end",
               "NOTAMODULO5":{
                     "TRABAJOS": 0,
                     "PRACTICA": 0,
                     "TEORIA": 0,
                     "TOTAL": 0.0                           
            },
         }
      }
   }
   return notas

def CambiarNota():
   # Esta funcion permite cambiar la nota del Camper
   db=js.ReadJson(js.JSON_CUENTAS)
   while True:
      mn.TitulasCambiarNotas()
      try:
         Camper = input('Ingrese el documento del camper')
         if Camper in db["CC"]:
            TipoModulo(Camper)
         else:
            print('Camper no encontrado..')
            Oprimir()
      except ValueError:
         print('Error')
   
def RegistrarNotas():
   db=js.ReadJson(js.JSON_CUENTAS)
   OrdenRegistroNotas()
   while True:
      mn.TitulasRegistroNotas()
      try:
         Camper = input('Ingrese el documento del camper')
         if Camper in db["CC"]:
            TipoModulo(Camper)
         else:
            print('Camper no encontrado..')
            Oprimir()
      except ValueError:
         print('Error')

def NuevaRuta():
  # Esta funcion permite crear una nueva ruta
  dbRutas = js.ReadJson(js.JSON_RUTAS)
  a= js.ReadJson(js.JSON_RUTAS)
  if len(a) == 3:
    print("Antes de crear una nueva ruta porfavor organice las 3 que ya existen")
    TrainerEncargado()
  else: 
    pass
  while True:
   clr() 
   print("Para crear una nueva ruta porfavor ingrese los siguientes datos: ")
   Oprimir()
   if len(dbRutas) == 12:
      print("Lo sentimos, no puede crear mas rutas, el maximo actual son 12")
      Oprimir()
      return
   else:
      resultadoFunc=SalaEntrenamientoYHorario()
      salon= resultadoFunc(0)
      horario= resultadoFunc(1)
      fechas=FechaFinal()
      fechaInicio=fechas(0)
      fechaFinalizacion=fechas(1)
      nombreRuta=NomRuta()
      Ruta = {
      nombreRuta:{
         "SALON":salon,
         "HORARIO":horario,
         "TRAINER":TrainerEncargado(nombreRuta),
         "CAMPERS":[],
         "FECHAINICIO":fechaInicio,
         "FECHAFINAL":fechaFinalizacion,
         "CAMPERSAPROVADOS": 0,
         "CAMPERSNOAPROVADOS": 0,  
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

def FechaInicio():
 while True: 
  fecha= date.today()
  print("Porfavor ingrese individualmente la fecha de inicio, siga el formato (Dia/Mes/Año)")
  dia=int(input)
  mes=int(input)
  if dia > 28 and mes == 2 or dia > 31 or dia < 0 or mes > 12 or mes < 0:
    print("La fecha ingresada es invalida, intentelo de nuevo")
    Oprimir()
    break
  else:
    pass 
  año=int(input)
  if año < fecha.year():
    print("Error, la fecha ingresada no es valida")
    Oprimir()
    break
  else: 
    return dia, mes,año
  
def FechaFinal():
 while True:
   fechaInit=FechaInicio()
   print("Porfavor ingrese individualmente la fecha de inicio, siga el formato (Dia/Mes/Año)")
   dia=int(input)
   mes=int(input)
   if dia > 28 and mes == 2 or dia > 31 or dia < 0 or mes > 12 or mes < 0:
      print("La fecha ingresada es invalida, intentelo de nuevo")
      Oprimir()
      break
   else:
      pass 
   año=int(input)
   if año < fechaInit(2):
      print("Error, la fecha ingresada no es valida")
      Oprimir()
      break
   else:
     fechaFinal=f"{dia}/{mes}/{año}"
     fechaInicial=f"{fechaInit(0)}/{fechaInit(1)}/{fechaInit(2)}"
     return fechaInicial, fechaFinal  

def NomRuta():
 while True:
   clr()
   dbRutas = js.ReadJson(js.JSON_RUTAS)
   NomRuta = str(input("Porfavor ingrese el nombre de la ruta que desea crear")).upper().strip()
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
            Oprimir()
            break
          else:
            salaYHorario=[salon,horario]
            return salaYHorario
    else:
      print("Porfavor elija un horario adecuado")
      Oprimir()

def TrainerEncargado(Ruta:str):
  while True:
    clr()
    VerTrainer()
    dbCuentas=js.ReadJson(js.JSON_CUENTAS)
    trainer=str(input(f"Porfavor ingrese el numero de identifiacion del trainer encargado al la ruta {Ruta}")).strip()
    if trainer in dbCuentas["TRAINERS"]:
      print("Trainer agregado correctamente")
      dbCuentas["TRAINERS"][trainer]["RUTA"].append(Ruta) 
      js.UpdateJson(js.JSON_CUENTAS, dbCuentas)
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

def AgregarARuta():
   dbCuentas=js.ReadJson(js.JSON_CUENTAS)
   dbRutas=js.ReadJson(js.JSON_RUTAS)
   while True:
      try:
         cc = int(input("Porfavor ingrese el numero de cedula del camper al que desea agregar"))
         if cc in dbCuentas["CAMPERS"]:
           if dbCuentas["CAMPERS"][cc]["ESTATUS"] == "APROVADO":
             while True:
               clr()
               VerRutas()
               ruta=str(input("Ingrese el nombre de la ruta al que desea agregar al camper: ")).upper().strip()
               if len(dbRutas[ruta]["CAMPERS"]) >= 33:
                  print(f"La ruta {ruta} se encuentra en su maxima capacidad")
                  Oprimir()
                  break
               else:
                 dbRutas[ruta]["CAMPERS"].append(cc)
                 dbCuentas["CAMPERS"][cc]["RUTA"] = ruta
                 dbCuentas["CAMPERS"][cc]["ESTATUS"] = "CURSANDO"
                 print(f"El camper identificado con {cc} a sido correctamente agregado a la ruta {ruta}")
                 js.UpdateJson(js.JSON_RUTAS, dbRutas)
                 return
      except:
        print("Ingrese solo numeros porfavor")
        Oprimir

def BorrarRuta():
 # Esta funcion permite borrar una ruta
 dbCuentas=js.ReadJson(js.JSON_CUENTAS)
 dbRutas=js.ReadJson(js.JSON_RUTAS)
 while True:
   clr()
   VerRutas()
   ruta = str(input("Ingrese el nombre de la ruta que desea eliminar: ")).strip().upper()
   if ruta in dbRutas:
      trainer= dbRutas[ruta]["TRAINER"]
      for i in dbRutas[ruta]["CAMPER"]:
         dbCuentas["CAMPERS"][i]["RUTA"] = None
      index=dbCuentas["TRAINER"][trainer]["RUTA"].index(ruta)
      del dbCuentas["TRAINER"][trainer]["RUTA"][index]  
      print(f"La ruta {ruta} ha sido eliminada correctamente")
      Oprimir()
      return  
   else: 
      print(f"La ruta {ruta} no ha sido encontrada")
      Oprimir() 

def EliminarDeRuta():
 # Esta funcion permite eliminar un camper de una ruta
 dbCuentas=js.ReadJson(js.JSON_CUENTAS)
 dbRutas=js.ReadJson(js.JSON_RUTAS)
 while True:
      try:
         cc = int(input("Porfavor ingrese el numero de cedula del camper al que desea eliminar de la ruta en la que se encuentra actualmente")).strip().upper()
         if cc in dbCuentas["CAMPERS"]:
           if dbCuentas["CAMPERS"][cc]["ESTATUS"] == "CURSANDO":
             while True:
               clr()
               ruta=dbCuentas["CAMPERS"][cc]["RUTA"]
               dbCuentas["CAMPERS"][cc]["RUTA"] = None
               dbRutas[ruta]["CAMPERS"].append(cc)
               print(f"El camper identificado con {cc} a sido correctamente elminado de la ruta {ruta}")
               js.UpdateJson(js.JSON_RUTAS, dbRutas)
               return
      except:
        print("Ingrese solo numeros porfavor")
        Oprimir

def CampersInscritos():
 # Esta funcion permite ver los campers inscritos
 campers=[]
 dbCuentas=js.ReadJson(js.JSON_CUENTAS)
 for i in dbCuentas["CAMPERS"]:
   if i["ESTATUS"]=="INSCRITO":
      campers.append(i)
   else:
     pass  
 print(f"Los campers inscritos son {campers}")      

def CampersAprobados():
 # Esta funcion permite ver los campers aprobados
 campers=[]
 dbCuentas=js.ReadJson(js.JSON_CUENTAS)
 for i in dbCuentas["CAMPERS"]:
   if i["ESTATUS"]=="APROVADO":
      campers.append(i)
   else:
     pass  
 print(f"Los campers aprovados son {campers}\nestos ya pueden ser inscritos a una ruta") 
 Oprimir()

def Trainers():
 # Esta funcion permite ver los trainers registrados
 trainers=[]
 dbCuentas=js.ReadJson(js.JSON_CUENTAS)
 for i in dbCuentas["TRAINERS"]:
   if i["ESTATUS"]=="ACTIVO":
      trainers.append(i)
   else:
     pass  
 print(f"Los trainers activos son: {trainers}") 
 Oprimir()
 

def CampersBajoRendimiento():
 # Esta funcion permite ver los campers con bajo rendimiento
 pass  

def CampersYTrainersMismaRuta():
 # Esta funcion permite ver los campers y trainers que estan en la misma ruta
 pass

def Estadisticas():
 # Esta funcion permite ver las estadisticas academicas
 pass


