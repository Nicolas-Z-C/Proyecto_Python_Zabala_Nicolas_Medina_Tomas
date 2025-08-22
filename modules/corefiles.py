import os
import time
import modules.json as js 
#Inicio de las funciones de la aplicacion

def clr(): 
 # Limpia la consola dependiendo del sistema operativo
 os.system('cls' if os.name == 'nt' else 'clear') 

def Wait(S:int):
 # Espera S segundos
 time.sleep(S)

def Oprimir():
 # Funcion para cuando hay un error con el usuario
 clr()
 input("Vuelva a intentarlo (Oprima una tecla para continuar")

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
 js.UpdateJson(js.JSON_CUENTAS,{"Trainers": Trainer})
 
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
     "Riesgo":Riesgo()

     }
    
    cuenta={cuentaNueva["CC"]:cuentaNueva}
    js.UpdateJson(js.JSON_CUENTAS,{"Camper": cuenta})
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
 db = js.ReadJson(js.JSON_CUENTAS)
 while True:
   cc=str(input("Porfavor ingrese la CC del estudiante que desea editar"))
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

def RegistroNotas():
   notas = {
      CC: {
         "Ruta": {
               "Modulos": {
                  "modulo 1": {
                     "Nombre": "Fundamentos la programacion",
                     "Notas": {
                           "Trabajos": None,
                           "Practica": None,
                           "Teoria": None,
                           "Total": None,
                     }
                  },
                  "modulo 2": {
                     "Nombre": "Progrmacion Web",
                     "Notas": {
                           "Trabajos": None,
                           "Practica": None,
                           "Teoria": None,
                           "Total": None,
                     }
                  },
                  "modulo 3": {
                     "Nombre": "Programacion Formal",
                     "Notas": {
                           "Trabajos": None,
                           "Practica": None,
                           "Teoria": None,
                           "Total": None,
                     }
                  },
                  "modulo 4": {
                     "Nombre": "Bases de datos",
                     "Notas": {
                           "Trabajos": None,
                           "Practica": None,
                           "Teoria": None,
                           "Total": None,
                     }
                  },
                  "modulo 5": {
                     "Nombre": "Back-end",
                     "Notas": {
                           "Trabajos": None,
                           "Practica": None,
                           "Teoria": None,
                           "Total": None,
                     }
                  }
               }
         }
      }
   }

def InitializeRutas():
   pass
def NuevaRuta():
 # Esta funcion permite crear una nueva ruta
 pass

def VerRutas():
 # Esta funcion permite ver las rutas creadas
 pass

def BorrarRuta():
 # Esta funcion permite borrar una ruta
 pass 

def AgregarARuta():
 # Esta funcion permite agregar un camper a una ruta
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



