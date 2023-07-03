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

            # Carga de datos
            arrays = load()
            if arrays != False:
              pinturas_db = arrays[0]
              indice_cotas = arrays[1]
              indice_nombres = arrays[2]

              print("")
              print("¡Carga de archivos lista!")
              print("")
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
                op2 = check_op(1, 3, '''Ingrese la opción de búsqueda que desea realizar:     
                            \n1.- Por cota
                            \n2.- Por nombre
                            \n3.- Volver al menú principal
                            \n-->''') 
                if op2 == 1:
                  cota = check_cota("Introduzca la cota de la pintura. \nDebe tener 4 letras seguido de 4 números. Ejemplo: 'ABDC1234'\n==>")
                  indice_pintura_array = search("cota", indice_cotas, 0, len(indice_cotas) - 1, cota)
                  indice_pintura = indice_pintura_array[0]
                  if indice_pintura != -1:
                    pintura_buscada = pinturas_db[indice_pintura]
                    pintura_buscada.showPintura()
                  else:
                    print("La pintura consultada no fue encontrada.")

                if op2 == 2:
                  nombre = (check_nom("Introduzca el nombre de la pintura (máx. 10 caracteres)\n==>")).lower().capitalize()
                  indice_pintura_array = search("nombre", indice_nombres, 0, len(indice_nombres) - 1, nombre)
                  indice_pintura = indice_pintura_array[0]
                  if indice_pintura != -1:
                    pintura_buscada = pinturas_db[indice_pintura]
                    pintura_buscada.showPintura()
                  else:
                    print("La pintura consultada no fue encontrada.")

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
                    op31 = check_op(1, 3, '''Ingrese la opción de búsqueda que desea realizar:     
                                \n1.- Por cota
                                \n2.- Por nombre
                                \n3.- Volver al menú anterior
                                \n-->''')
                    
                    if op31 == 1:
                      cota = check_cota("Introduzca la cota de la pintura. \nDebe tener 4 letras seguido de 4 números. Ejemplo: 'ABDC1234'\n==>")
                      indice_pintura_array = search("cota", indice_cotas, 0, len(indice_cotas) - 1, cota)
                      indice_pintura = indice_pintura_array[0]
                      if indice_pintura != -1:
                        pintura_buscada = pinturas_db[indice_pintura]
                        pintura_buscada.changeStatus("En exhibición")
                      else:
                        print("La pintura consultada no fue encontrada.")
                    
                    if op31 == 2:
                      nombre = (check_nom("Introduzca el nombre de la pintura (máx. 10 caracteres)\n==>")).lower().capitalize()
                      indice_pintura_array = search("nombre", indice_nombres, 0, len(indice_nombres) - 1, nombre)
                      indice_pintura = indice_pintura_array[0]
                      if indice_pintura != -1:
                        pintura_buscada = pinturas_db[indice_pintura]
                        pintura_buscada.changeStatus("En exhibición")
                      else:
                        print("La pintura consultada no fue encontrada.")
                    
                    if op31 == 3:
                       pass

                if op3 == 2:    
                    op32 = check_op(1, 3, '''Ingrese la opción de búsqueda que desea realizar:     
                                \n1.- Por cota
                                \n2.- Por nombre
                                \n3.- Volver al menú anterior
                                \n-->''')
                    
                    if op32 == 1:
                      cota = check_cota("Introduzca la cota de la pintura. \nDebe tener 4 letras seguido de 4 números. Ejemplo: 'ABDC1234'\n==>")
                      indice_pintura_array = search("cota", indice_cotas, 0, len(indice_cotas) - 1, cota)
                      indice_pintura = indice_pintura_array[0]
                      if indice_pintura != -1:
                        pintura_buscada = pinturas_db[indice_pintura]
                        pintura_buscada.changeStatus("En mantenimiento")
                      else:
                        print("La pintura consultada no fue encontrada.")
                    
                    if op32 == 2:
                      nombre = (check_nom("Introduzca el nombre de la pintura (máx. 10 caracteres)\n==>")).lower().capitalize()
                      indice_pintura_array = search("nombre", indice_nombres, 0, len(indice_nombres) - 1, nombre)
                      indice_pintura = indice_pintura_array[0]
                      if indice_pintura != -1:
                        pintura_buscada = pinturas_db[indice_pintura]
                        pintura_buscada.changeStatus("En mantenimiento")
                      else:
                        print("La pintura consultada no fue encontrada.")
                    
                    if op32 == 3:
                       pass

                if op3 == 3:
                  break      
            
            #Eliminacion logica de la pintura
        if op == 4:     
          while True:    
            op4 = check_op(1, 3, '''Ingrese la opción de búsqueda que desea realizar:     
                        \n1.- Por cota
                        \n2.- Por nombre
                        \n3.- Volver al menú principal
                        \n-->''')

            if op4 == 1:
              cota = check_cota("Introduzca la cota de la pintura. \nDebe tener 4 letras seguido de 4 números. Ejemplo: 'ABDC1234'\n==>")
              indice_pintura_array = search("cota", indice_cotas, 0, len(indice_cotas) - 1, cota)
              indice_pintura = indice_pintura_array[0]
              if indice_pintura != -1:
                pintura_buscada = pinturas_db[indice_pintura]
                pintura_buscada.deleteLogical(False)
              else:
                print("La pintura consultada no fue encontrada.")
            
            if op4 == 2:
              nombre = (check_nom("Introduzca el nombre de la pintura (máx. 10 caracteres)\n==>")).lower().capitalize()
              indice_pintura_array = search("nombre", indice_nombres, 0, len(indice_nombres) - 1, nombre)
              indice_pintura = indice_pintura_array[0]
              if indice_pintura != -1:
                pintura_buscada = pinturas_db[indice_pintura]
                pintura_buscada.deleteLogical(False)
              else:
                print("La pintura consultada no fue encontrada.")
            
            if op4 == 3:
              break
           
            #Compactacion
        if op == 5:
          op5 = check_op(1, 2, '''¿Está seguro/a de proseguir con la compactación?:     
                        \n1.- Si
                        \n2.- No
                        \n-->''')
          if op5 == 1:
            num = 0
            while num < len(pinturas_db):
              picture = pinturas_db[num]
              nombre = picture.nombre
              cota = picture.cota
              indice_nombre_array = search("nombre", indice_nombres, 0, len(indice_nombres) - 1, nombre)
              nombre_index = indice_nombre_array[1]
              indice_cota_array = search("cota", indice_cotas, 0, len(indice_cotas) - 1, cota)
              cota_index = indice_cota_array[1]
              if picture.exists == True:
                indice_nombres[nombre_index].update({"posicion": num})
                indice_cotas[cota_index].update({"posicion": num})
                picture.showPintura()
                num += 1
              else:
                del pinturas_db[num]
                del indice_nombres[nombre_index]
                del indice_cotas[cota_index]
            print("¡Compactación terminada!")

        if op == 6:   #Salir de la aplicación y guardar en txt
            save(pinturas_db, indice_cotas, indice_nombres)
            print("""
            ¡Hasta pronto!
            """)
            break
        
main()