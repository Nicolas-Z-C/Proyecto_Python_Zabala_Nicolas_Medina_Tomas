import modules.corefiles as core
import modules.menufiles as menus
import modules.Js as Js
if __name__ == "__main__":
 print("""
       -------------------------------------------------------------
       |***Bienvenido al sistema de gestion de campers y trainers***|
       -------------------------------------------------------------
       """)
 core.Wait(1)
 core.clr()
 contador = 0

 a=core.js.ReadJson(core.js.JSON_CUENTAS)
 if a == {}:
  contador = True

 if contador == True:
   core.IniciarJsons1()
   core.IniciarJsons2()
 else:
   pass
 core.Login()
 if contador == True:
   core.clr()
   print("Al ser la primera vez porfavor ingrese los suigientes datos")
   core.IniciarJsonRutas()
 else:
   pass
 contador=False
 while True:
  core.clr()
  menus.MainMenu()
  try:
    op = int(input('Ingrese la opcion que desee.\nOpcion: '))
    match op:
      case 1:
        core.CrearCuenta()
      case 2:
        core.AgregarTrainer()
      case 3:
        core.CambiarEstatusCamper()
      case 4:
        core.RegistrarNotas()
      case 5:
        core.CambiarNotas()
      case 6:
        core.MatricularCampers()
      case 7:
        core.CrearNuevaRuta()
      case 8:
        core.VerNotas()
      case 9:
        core.BorrarCuentaCamper()
      case 10:
        core.BorrarCuentaTrainer()
      case 11:
        print("Saliendo del sistema...")
        break
      case _:
        print("Opcion no valida, por favor intente de nuevo.")
  except ValueError:
    print('Error: Solo se puedene ingrasar numeros..')
    core.Oprimir()