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
    core.AgregarTrainer()
  case "3":
    core.CambiarEstatusCamper()
  case "4":
    core.CambiarNotas()
  case "5":
    core.CrearNuevaRuta()
  case "6":
    core.MatricularCampers()
  case "7":
    core.VerNotas()
  case "8":
    core.BorrarCuentaCamper()
  case "9":
    core.BorrarCuentaTrainer()
  case "10":
    print("Saliendo del sistema...")
    break
  case _:
    print("Opcion no valida, por favor intente de nuevo.")
  