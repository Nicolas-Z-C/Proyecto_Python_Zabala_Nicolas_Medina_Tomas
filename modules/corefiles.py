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
 clr()
 input("La opcion ingresada no es valida, vuelva a intentarlo (Oprima una tecla para continuar)")

def CrearCuenta():
 # Esta funcion permite crear una cuenta de usuario sea trainer o camper
 cuenta={}
 while True:
    db=js.ReadJson(js.)
    llave=
    print("""
        ---------------------------------------------------------
        |A continuacion porfavor ingrese los datos de los campers
        ---------------------------------------------------------
        """)
    
 
 pass

def Nombre():
 # Esta funcion permite ingresar el nombre del usuario
 while True:
    clr()
    try:
        Nombre=str(input("Porfavor ingrese el nombre del camper: "))
        if Nombre.isalpha():
         return Nombre
        else:
         Oprimir()
    except ValueError:
     Oprimir
    

def CC():
 # Esta funcion permite ingresar el numero de cedula del usuario
 while True:
  clr()
  try:
   cc=int(input("Porfavor ingrese su numero de cedula"))
   return cc
  except ValueError:
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
   Oprimir()
  else:
   return NomAcu

def Telefono():
 # Esta funcion permite ingresar el telefono del usuario
 pass

def Estatus():
 # Esta funcion permite ingresar el estatus del usuario
 pass

def Riesgo():
 # Esta funcion permite ingresar el nivel de riesgo del usuario
 pass

def Login():
 # Esta funcion permite iniciar sesion en la aplicacion
 pass

def Logout():
 # Esta funcion permite cerrar sesion en la aplicacion
 pass

def BorrarCuenta():
 # Esta funcion permite borrar una cuenta de usuario sea trainer o camper
 pass

def CambiarContraseña():
 # Esta funcion permite cambiar la contraseña del usuario
 pass

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



