import modules.corefiles as core
import modules.menufiles as menus
if __name__ == "__main__":
 print("""
       -------------------------------------------------------------
       |***Bienvenido al sistema de gestion de campers y trainers***|
       -------------------------------------------------------------
       """)
 core.Wait(1)

while True:
 core.clr()

 op = menus.MainMenu()
 match op:
  case "1":
    core.CrearCuenta()
  case "2":
    core.CambiarEstatusCamper()
  case "3":
    core.CambiarNotas()
  case "4":
    core.CrearNuevaRuta()
  case "5":
    core.MatricularCampers()
  case "6":
    core.Reportes()
  case "7":
    core.BorrarCuenta()
  case "8":
    print("Saliendo del sistema...")
    break
  case _:
    print("Opcion no valida, por favor intente de nuevo.")
  