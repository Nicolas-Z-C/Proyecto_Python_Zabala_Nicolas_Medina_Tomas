import modules.corefiles as core
import modules.menufiles as mn
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
 else:
   pass
 core.Login()
 contador=False
 while True:
  core.clr()
  mn.MainMenu()
  try:
    op = int(input('Ingrese la opcion que desee.\nOpcion: '))
    match op:
      case 1:
        while True:
          mn.MenuGestorCuentas()
          op = int(input('Ingrese la opcion que desee.\nOpcion: '))
          match op:
            case 1:
              core.CrearCuenta()
            case 2:
              core.AgregarTrainer()
            case 3:
              core.EditarEstatus()
            case 4:
              core.EditarEstatusTrainer()
            case 5:
              print('Saliendo del sistema...')
              break
            case _:
              print('Opcion ingresada no disponible..')
              core.Oprimir()
      case 2:
        while True:
          mn.MenuGestorAcademico()
          op = int(input('Ingrese la opcion que desee.\nOpcion: '))
          match op:
            case 1:
              core.RegistrarNotas()
            case 2:
              core.AgregarARuta()
            case 3:
              core.NuevaRuta()
            case 4:
              print('Saliendo del sistema...')
              break  
            case _:
              print('Opcion ingresada no disponible..')
              core.Oprimir()
      case 3:
        mn.MenuReportes()
        op = int(input('Ingrese la opcion que desee.\nOpcion: '))
        match op:
          case 1:
            core.CampersInscritos()
          case 2:
            core.CampersAprobados()
          case 3:
            core.Trainers()
          case 4:
            core.CampersBajoRendimiento()
          case 5:
            core.CampersYTrainersMismaRuta()
          case 6:
            print('Saliendo del sistema...')
            Repetir = 'n'
            break
          case _:
            print('Opcion ingresada no disponible..')
            core.Oprimir()
      case 4:
        print('Saliendo del sistema..')
      case _:
        print("Opcion no valida, por favor intente de nuevo.")
  except ValueError:
    print('Error: Solo se puedene ingrasar numeros..')
    core.Oprimir()