
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

def check_let(msg):
    while True:
        print("")
        word = input(msg)
        if word.replace(" ", "").replace("&", "").isalpha():
             break
        else:
            print("Error, ingrese un nombre valido")
            continue
    return word