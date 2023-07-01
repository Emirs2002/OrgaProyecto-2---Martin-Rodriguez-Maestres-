from tools import *

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
            print("mango txt mango")


          #Insertar pinturas en la bd e indices
        if op == 1:           
            print("a")

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