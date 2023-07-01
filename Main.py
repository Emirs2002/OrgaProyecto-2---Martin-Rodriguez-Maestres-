from tools import *
from Pintura import Pintura

def main():
    pinturas_db = []
    indice_cotas = []
    indice_nombres = []
    

    while True:

        print("")
        print("***BIENVENIDO AL HIMALAYA***")
        print("")
                              #Menú principal
        op = check_op(0, 6, '''Ingrese la opción que desea realizar:
            \n0.- Cargar Datos
            \n1.- Insertar pintura
            \n2.- Consultar pintura
            \n3.- Cambiar status
            \n4.- Eliminar pintura
            \n5.- Compactar
            \n6.- Guardar y Salir
            \n==>''') 
        if op == 0:
            for pint in range(len(pinturas_db)):
               pintura = pinturas_db[pint]
               print(f"PINTURA {pint+1}")
               pintura.showPintura()
               print("")
               print("")
               


          #Insertar pinturas en la bd e indices
        if op == 1:           
            cota = check_cota("Introduzca la cota de la pintura. \nDebe tener 4 letras seguido de 4 números. Ejemplo: 'ABDC1234'\n==>")
            nombre = check_nom("Introduzca el nombre de la pintura (máx. 10 caracteres)\n==>")
            precio = check_num(False, "Introduzca el precio de la pintura\n==>")
            anho = check_num(True, "Introduzca el año de la pintura. Ejemplo '2023'\n==>")
            status = check_status('''Indique el estado de la pintura
                                  \n1.- En mantenimiento
                                  \n2.- En exhibición
                                  \n==>''')
            
            pintura = Pintura(cota, nombre.capitalize(), precio, anho, status, True)

            pinturas_db.append(pintura)

          #Consultar pinturas
        if op == 2:  
              while True:    
                op2 = check_op(1, 3, '''Ingrese la opción que desea realizar:     
                            \n1.- Por cota
                            \n2.- Por nombre
                            \n3.- Volver al menú principal
                            \n-->''') 
                if op2 == 1:
                  print('por cota')   

                if op2 == 2:
                  print('por nombre')   

                if op2 == 3:
                  break                   
            
            #Cambiar status
        if op == 3:      
           
            while True:   
                op3 = check_op(1, 4, '''Ingrese la opción que desea realizar:     
                            \n1.- Poner en exhibicion
                            \n2.- Poner en mantenimiento
                            \n3.- Volver al menú principal
                            \n-->''')                            
                if op3 == 1:
                  print('exhibicion')   

                if op3 == 2:
                  print('mantenimiento')   

                if op3 == 3:
                  break      
            
            #Eliminacion logica de la pintura
        if op == 4:     

          print("a")
           
            #Compactacion
        if op == 5:  
          print("a")
            

        if op == 6:   #Salir de la aplicación y guardar en txt
            print("¡Hasta pronto!")
            break
        
main()