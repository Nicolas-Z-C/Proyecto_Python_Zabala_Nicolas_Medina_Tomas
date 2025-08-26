def notatotal(cc):
    print(cc)
def modulo(cc):
    print(cc)
    notatotal(cc)
def cc():
    cc = '123'
    modulo(cc)

cc()
while True:
    try:
      op = int(input("""
      --------------------------------------------------------------------
      | Ingrese porfavor el tipo de telefono que se registrara al camper 
      |                                                                  
      | 1. Movil                                                         
      | 2. Fijo                                                          
      |                                                                  
      --------------------------------------------------------------------        
      : """))
      match op: 
         case 1:
            numero=str(input("Digite el telefono movil del camper: "))
            if len(numero) != 10:
                continue
            else: 
                pass
         case 2:
            numero=str(input("Digite el telefono fijo del camper: "))
            if len(numero) != 8: 
                continue
            else: 
                pass
         case _:
            Oprimir()
    except ValueError:
       print('Error: Solo se pueden ingresar numeros.')
       input('')
       