
#####       VALIDACIONES      #####

#validar números en un rango específico

def check_op(lim1, lim2, msg):
    while True:
        print("")
        num = input(msg)        
        if num.replace(" ", "").isnumeric():
            num = int(num)
            if num < lim1 or num > lim2:
                print("Error, ingrese un numero valido")
                continue
            else:
                break
        else:
            print("Error, ingrese un numero")
            continue    
    return num

#validar palabras

def check_nom(msg):
    while True:
        print("")
        word = input(msg)
        #validar que sea letra, max 10 letras y que no haya espacios
        if word.isalpha() and len(word) <= 10 and " " not in word:
             break
        else:
            print("Error, ingrese un nombre valido")
            continue
    return word

#validar números 

def check_num(anho, msg):
    while True:
        print("")
        num = input(msg)   
        if (num.replace(",", "").isnumeric()) and (" " not in num) and (int(num)>0):
            if anho == True:
                if len(num) != 4:
                    print("Introduzca un año valido")
                    continue
                else: 
                    break
            break
        else:
                print("Error, ingrese un numero")
                continue    
    return num

#valir el estado de la pintura

def check_status(msg):
    while True:
        op = check_op(1,2,msg)
        
        if op == 1:
            status = "En mantenimiento"
            break

        if op == 2:
            status = "En exhibición"
            break

    return status


#Validar la cota ingresada por el usuario
def check_cota(msg):
    cotaValida = True
    cota = input(msg)
    cotaNew = "" #string donde se va a guardar la cota con las letras en mayuscula
    while True:
        print("")
        if (cota.isalnum()) and (len(cota) == 8) and (cotaValida == True):
            
            #Validar que los primeros 4 caracteres sean letras
            for let in range(0, 4):
                letter = cota[let]
                if letter.isalpha():
                   cotaNew += letter.upper()
                   pass
                else:
                    cotaValida = False
                    break
            
            #Validar que los siguientes 4 caracteres sean numeros
            if cotaValida == True:
                for num in range(4,8):
                    number = cota[num]
                    if number.isnumeric():
                        cotaNew += number
                        pass
                    else:
                        cotaValida = False
                        break

                 #ultima validacion para devolver la cota o un error
                if cotaValida == True:
                    break
                else:
                    pass

            else:
                pass

        else: 
            print("Error, ingrese una cota valida")
            cotaValida = True
            cota = input(msg)
            cotaNew = ""
            continue
    
    return cotaNew