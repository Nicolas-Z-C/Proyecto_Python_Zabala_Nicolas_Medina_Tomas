
import modules.corefiles as core 

def MainMenu():
    core.clr()
    print("""
    --------------------------------------------
        **** Menu Principal ****       
    --------------------------------------------
        1. Crear Cuenta (Camper)
        2. Crear Cuenta (Trainer)  
        3. Cambiar Estatus Camper
        4. Registrar Notas
        5. Cambiar Notas
        6. Matricular Campers
        7. Crear Nueva Ruta
        8. Reportes
        9. Borrar Cuenta(Camper)
       10. Borrar Cuenta(Camper) 
       11. Salir   
    --------------------------------------------
    """)
    
def Modulos():
    core.clr()    
    print("""
----------------------------------------
|               MODULOS                |
----------------------------------------
    1. Fundamentos la programacion
    2. Progrmacion Web
    3. Programacion Formal
    4. Bases de datos
    5. Back-end
----------------------------------------
              """)
        
def MenuTipoNota():
    core.clr()
    print("""
----------------------------------------
|           Tipos De Notas             |
----------------------------------------
    1. Nota Teoria
    2. Nota Practica
    3. Nota Trabajo
----------------------------------------

          """)