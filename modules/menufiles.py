
import modules.corefiles as core 

def MainMenu():
    core.clr()
    print("""
-----------------------------------
|         Menu Principal          |
-----------------------------------
|   1. Gestor Cuentas             |
|   2. Gestor Academico           |
|   3. Reportes                   |
|   4. Salir                      |                        
-----------------------------------
    """)
def MenuGestorCuentas():
    core.clr()
    print("""
-----------------------------------
|         Gestor Cuentas          |
-----------------------------------
|   1. Crear Cuenta Camper        |
|   2. Crear Cuenta Trainer       |
|   3. Cambiar Estatus Camper     |
|   5. Cambiar Estatus Trainer    |
|   4. Salir                      |                        
-----------------------------------
          """)
def MenuGestorAcademico():
    core.clr()
    print("""
----------------------------------- 
|        Gestor Academico         |
-----------------------------------
|   1. Registrar Notas Campers    |
|   2. Matriculas Campers         |
|   3. Nueva Ruta                 |
|   4. Salir                      |
|                                 |                        
-----------------------------------

          """)
def MenuReportes():
    core.clr()
    print("""
-----------------------------------
|           Reportes              |
-----------------------------------
|   1. Campers Inscritos          |
|   2. Campers Aprobado           |
|   3. Trainer Activo             | 
|   4. Campers Bajo Rendimiento   |
|   5. Campers Rutas              |
|   6. Salir                      |                        
-----------------------------------
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
def TitulasCambiarNotas():
    core.clr()
    print("""
--------------------------------------
|    Bienvenido a Cambiar Notas    | 
--------------------------------------
          """)
def TitulasCrearRuta():
    core.clr()
    print("""
--------------------------------------
|      Bienvenido a Crear Notas      | 
--------------------------------------
          """)
def TitulasRegistroNotas():
    core.clr()
    print("""
--------------------------------------
|    Bienvenido a Registrar Notas    | 
--------------------------------------
          """)