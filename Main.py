from tools import *
from Pintura import Pintura

def main():
    #DECLARACION LISTAS
    pinturas_db = []
    indice_cotas = []
    indice_nombres = []

    pintura_pos = 0  #guardar la posicion de la pintura para insertarlo en los indices

    while True:

        print("")
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
            #ESTE CODIGO ES PARA VER SI TODO SE ESTA GUARDANDO CORRECTAMENTE, LQM
            for pint in range(len(pinturas_db)):
               pintura = pinturas_db[pint]
               print(f"PINTURA {pint+1}")
               pintura.showPintura()
               print("")
               print("")
            
            for cot in range(len(indice_cotas)):
               cota = indice_cotas[cot]
               print(cota)

            print("")
            print("")
            print("")
               
            for nom in range(len(indice_nombres)):
               nombre = indice_nombres[nom]
               print(nombre)

          #Insertar pinturas en la bd e indices
        if op == 1:       
            #todas las validaciones e inserciones estan en el archivo tools  
            alreadyExists = False
            while True:
              
              cota = check_cota("Introduzca la cota de la pintura. \nDebe tener 4 letras seguido de 4 números. Ejemplo: 'ABDC1234'\n==>")
              alreadyExists = check_list("cota", cota, indice_cotas)

              if alreadyExists == True:
                print("Error, la cota ingresada pertenece a otra pintura. Ingrese otra cota nuevamente.")
                print("")
              else:
                 break
            
            while True:
              nombre = (check_nom("Introduzca el nombre de la pintura (máx. 10 caracteres)\n==>")).lower().capitalize()
              alreadyExists = check_list("nombre", nombre, indice_nombres)

              if alreadyExists == True:
                print("Error, el nombre ingresado pertenece a otra pintura. Por favor, ingrese otro nombre.")
                print("")
              else:
                break
            
            precio = check_num(False, "Introduzca el precio de la pintura\n==>")
            anho = check_num(True, "Introduzca el año de creación de la pintura. Ejemplo '2023'\n==>")
            status = check_status('''Indique el estado de la pintura
                                  \n1.- En mantenimiento
                                  \n2.- En exhibición
                                  \n==>''')
            
            pintura = Pintura(cota, nombre, precio, anho, status, True)

            #insercion de la pintura en la lista
            pinturas_db, pintura_pos = insertPainting(pintura,pinturas_db)             

            #insercion de su referencia en los indices correspondientes
            indice_cotas = insertIdIndex(cota, pintura_pos, indice_cotas)
            indice_nombres = insertNameIndex(nombre, pintura_pos, indice_nombres)

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