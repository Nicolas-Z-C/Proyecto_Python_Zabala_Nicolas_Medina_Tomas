import os
import json
from typing import Dict, List, Optional, Any, Union, Callable


JSON_CUENTAS = "data/JsonCuentas.json"
JSON_NOTAS = "data/JsonNotas.json"
JSON_RUTAS = "data/JsonRutas.json"

def ReadJson(file_path: str)-> Dict:
    try:
        with open(file_path, "r", encoding="utf-8") as ArchivoJson:
            return json.load(ArchivoJson)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}
    
def WriteJson(file_path: str, data: Dict) -> Dict:
    with open(file_path, "w", encoding="utf-8") as ArchivoJson:
        json.dump(data, ArchivoJson, indent=4)
#Arreglar esta mierda
def UpdateJson(file_path: str, data: Dict, path: Optional[list[str]] =None ) -> None:
    CurrentData = ReadJson(file_path)

    if not isinstance(CurrentData, dict):
        CurrentData = {}

    if not path:
        CurrentData.update(data)
    else:
        current = CurrentData
        for key in path[:-1]:
            current = current.setdefault(key, {})
        current.setdefault(path[-1], {}).update(data)
    WriteJson(file_path, CurrentData)

def InitJson(file_path: str, initial_structure: Dict) -> None:
    if not os.path.isfile(file_path):
        WriteJson(file_path, initial_structure)
    else:
        current_data = ReadJson(file_path)
        for key, value in initial_structure.items():
            if key not in current_data:
                current_data[key] = value
        WriteJson(file_path, current_data)



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
        "TRAINERS": {}
    }
 a = {}
 InitJson(JSON_NOTAS, a)
 InitJson(JSON_CUENTAS, estructuraInicialCuentas)
  
def IniciarJsonRutas():
 fechas= FechaFinal()
 fechaInicio=fechas(0)
 fechaFinalizacion=fechas(1)      
 estructuraInicialRutas={
        "NODEJS": {
         "MODULOS":{
             "MODULO1":"Fundamentos la programacion",
                  "MODULO2":"Programacion Web",
                  "MODULO3":"Programacion Formal",
                  "MODULO4":"Bases de datos",
                  "modulo 5":"Back-end"
         },
         "SALON":"W1",
         "HORARIO":1,
         "TRAINER":None,
         "CAMPERS":{},
         "FECHAINICIO":fechaInicio,
         "FECHAFINAL": fechaFinalizacion,  
        },
        "JAVA": {
         "MODULOS":{
             "MODULO1":"Fundamentos la programacion",
                  "MODULO2":"Programacion Web",
                  "MODULO3":"Programacion Formal",
                  "MODULO4":"Bases de datos",
                  "modulo 5":"Back-end"
         },
         "SALON":"W2",
         "HORARIO":1,
         "TRAINER":None,
         "CAMPERS":{
             "MODULO1":"Fundamentos la programacion",
                  "MODULO2":"Programacion Web",
                  "MODULO3":"Programacion Formal",
                  "MODULO4":"Bases de datos",
                  "modulo 5":"Back-end"
         },
         "FECHAINICIO":fechaInicio,
         "FECHAFINAL": fechaFinalizacion,  
        },
        "NETCORE": {
         "MODULOS":{
             "MODULO1":"Fundamentos la programacion",
                  "MODULO2":"Programacion Web",
                  "MODULO3":"Programacion Formal",
                  "MODULO4":"Bases de datos",
                  "modulo 5":"Back-end"
         },
         "SALON":"W3",
         "HORARIO":1,
         "TRAINER":None,
         "CAMPERS":{},
         "FECHAINICIO":fechaInicio,
         "FECHAFINAL": fechaFinalizacion,  
        },  
    }

 InitJson(JSON_RUTAS, estructuraInicialRutas)



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
     "RUTA": None 
     }
    
 Trainer={TrainerNuevo["CC"]:TrainerNuevo}
 UpdateJson(JSON_CUENTAS,Trainer,["TRAINERS"])

def OrdenRegistroNotas(CC: str):
   notas = {
      "4": {
         "MODULOS": {
            "MODULOS 1": "FUNDAMENTOS DE LA PROGRAMACION",
            "NOTAS": {
                     "TRABAJOS": 0,
                     "PRACTICA": 0,
                     "TEORIA": 0,
                     "TOTAL": 0.0
               },
            "MODULO 2" : "PROGRAMACION WEB",
            "NOTA2":{
                     "TRABAJOS": 0,
                     "PRACTICA": 0,
                     "TEORIA": 0,
                     "TOTAL": 0.0                           
            },
            "MODULO 3" : "PROGRAMACION WEB",
            "NOTA3":{
                     "TRABAJOS": 0,
                     "PRACTICA": 0,
                     "TEORIA": 0,
                     "TOTAL": 0.0                           
            },
            "MODULO 4" : "BASE DE DATOS",
            "NOTA4":{
                     "TRABAJOS": 0,
                     "PRACTICA": 0,
                     "TEORIA": 0,
                     "TOTAL": 0.0                           
            },
            "MODULO 5" : "back-end",
            "NOTA5":{
                     "TRABAJOS": 0,
                     "PRACTICA": 0,
                     "TEORIA": 0,
                     "TOTAL": 0.0                           
            }
         }
      }
   }
   print(notas)
   return notas

def CrearCuenta():
 # Esta funcion permite crear una cuenta de usuario sea trainer o camper
 cuenta={}
 while True:
    print("""
        ---------------------------------------------------------
        |A continuacion porfavor ingrese los datos de los campers
        ---------------------------------------------------------
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
    UpdateJson(JSON_CUENTAS,cuenta,["CAMPERS"])
    UpdateJson(JSON_NOTAS,OrdenRegistroNotas(cuentaNueva["CC"]))
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
    return Nombre
   

def CC():
 # Esta funcion permite ingresar el numero de cedula del usuario
 while True:
  cuentas=ReadJson(JSON_CUENTAS)
  clr()
  try:
   cc=int(input("Porfavor ingrese su numero de cedula: "))
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
  dir=str(input("Porfavor ingresa la direccion de residencia del camper: "))
  return dir

def Acudiente():
 # Esta funcion permite ingresar el nombre del acudiente del usuario
 while True:
  clr()
  NomAcu=str(input("Porfavor ingrese el nombre del acudiente del camper: "))
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
    : """)
    match op: 
     case "1":
        numero=str(input("Digite el telefono movil del camper: "))
        if len(numero) != 10:
         Oprimir()
        else: 
         return numero
     case "2":
        numero=str(input("Digite el telefono fijo del camper: "))
        if len(numero) != 8:
         Oprimir()
        else: 
         return numero
     case _:
      Oprimir()

def EditarEstatus():
 # Esta funcion permite editar el estatus de un camper
 db = ReadJson(JSON_CUENTAS)
 while True:
   cc=str(input("Por favor ingrese la CC del estudiante que desea editar"))
   if cc in db["CAMPERS"]: 
      status=str(input("Ahora ingrese el nuevo estatus del estudiante"))
      db["CAMPERS"][cc]["ESTATUS"] = status 
      UpdateJson(JSON_CUENTAS, db,)
      return 
   else:
      print("La cedula ingresada no se encuentra registrada")
      Oprimir()

OrdenRegistroNotas(4)





