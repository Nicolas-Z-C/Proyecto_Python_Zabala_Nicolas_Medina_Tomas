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
 Repetir = 's'
 while Repetir == 's':
  core.clr()
  mn.MainMenu()
  try:
    op = int(input('Ingrese la opcion que desee.\nOpcion: '))
    match op:
      case 1:
        mn.MenuGestorCuentas()
        op = int(input('Ingrese la opcion que desee.\nOpcion: '))
        match op:
          case 1:
            pass
          case 2:
            pass
          case 3:
            pass
          case 4:
            print('Saliendo del sistema...')
            Repetir = 'n'
            break
          case _:
            print('Opcion ingresada no disponible..')
            core.Oprimir()
      case 2:
        mn.MenuGestorAcademico()
        op = int(input('Ingrese la opcion que desee.\nOpcion: '))
        match op:
          case 1:
            pass
          case 2:
            pass
          case 3:
            pass
          case 4:
            pass
          case 5:
            print('Saliendo del sistema...')
            Repetir = 'n'
            break
          case _:
            print('Opcion ingresada no disponible..')
            core.Oprimir()
      case 3:
        mn.MenuReportes()
        op = int(input('Ingrese la opcion que desee.\nOpcion: '))
        match op:
          case 1:
            pass
          case 2:
            pass
          case 3:
            pass
          case 4:
            pass
          case 5:
            pass
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