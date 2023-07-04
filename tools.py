import pickle

#####       VALIDACIONES      #####

# validar números en un rango específico


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


# validar palabras


def check_nom(msg):
    while True:
        print("")
        word = input(msg)
        # validar que sea letra, max 10 letras y que no haya espacios
        if word.isalpha() and len(word) <= 10 and " " not in word:
            break
        else:
            print("Error, ingrese un nombre valido")
            continue
    return word


# validar números


def check_num(anho, msg):
    while True:
        print("")
        num = input(msg)
        if (num.isnumeric()) and (" " not in num) and (int(num) > 0):
            if anho == True:
                if (len(num) != 4) or (int(num) > 2023):
                    print("Introduzca un año valido")
                    continue
                else:
                    break
            break
        else:
            print("Error, ingrese un numero")
            continue
    return num


# validar el estado de la pintura


def check_status(msg):
    while True:
        op = check_op(1, 2, msg)

        if op == 1:
            status = "En mantenimiento"
            break

        if op == 2:
            status = "En exhibición"
            break

    return status


# Validar la cota ingresada por el usuario
def check_cota(msg):
    cotaValida = True
    cota = input(msg)
    cotaNew = ""  # string donde se va a guardar la cota con las letras en mayuscula

    while True:
        print("")
        if (cota.isalnum()) and (len(cota) == 8) and (cotaValida == True):
            # Validar que los primeros 4 caracteres sean letras
            for let in range(0, 4):
                letter = cota[let]
                if letter.isalpha():
                    cotaNew += letter.upper()
                    pass
                else:
                    cotaValida = False
                    break

            # Validar que los siguientes 4 caracteres sean numeros
            if cotaValida == True:
                for num in range(4, 8):
                    number = cota[num]
                    if number.isnumeric():
                        cotaNew += number
                        pass
                    else:
                        cotaValida = False
                        break

                # ultima validacion para devolver la cota o un error
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


# VERIFICAR QUE LA COTA Y EL NOMBRE NO ESTEN REPETIDOS


def check_list(tipo, valor, indice_lista):
    alreadyExists = False

    if tipo == "cota":
        for cot in range(len(indice_lista)):
            cotaDic = indice_lista[cot]
            if cotaDic["cota"] == valor:
                alreadyExists = True
    else:
        for nom in range(len(indice_lista)):
            nomDic = indice_lista[nom]
            if nomDic["nombre"] == valor:
                alreadyExists = True

    return alreadyExists


#####           INSERCION PINTURAS      ######


def insertPainting(painting, painting_db):
    if len(painting_db) == 0:
        pintura_pos = 0
        painting_db.append(painting)
    else:
        pintura_pos = len(painting_db)
        painting_db.append(painting)

    return painting_db, pintura_pos


#####       INSERCION DE ELEMENTOS EN LOS INDICES       ######

# INDICE DE LAS COTAS


def insertIdIndex(cota, pos, indice_cotas):
    dicCota = {"cota": cota, "posicion": pos}

    indice_cotas.append(dicCota)

    sorted_indice_cotas = sorted(
        indice_cotas, key=lambda x: x["cota"]
    )  # ordenar la lista de menor a mayor por valor de cota

    return sorted_indice_cotas


# INDICE DE LOS NOMBRES
def insertNameIndex(nombre, pos, indice_nombres):
    dicName = {"nombre": nombre, "posicion": pos}

    indice_nombres.append(dicName)

    sorted_indice_nombres = sorted(
        indice_nombres, key=lambda x: x["nombre"]
    )  # ordenar el la lista de menor a mayor por valor de nombre

    return sorted_indice_nombres


#####       BÚSQUEDA       ######


# Segun el tipo de indice (index_type)
def search(index_type, array, first, last, x):
    if first <= last:
        mid = (first + last) // 2
        if x == array[mid][index_type]:
            return [array[mid]["posicion"], mid]
        if x < array[mid][index_type]:
            return search(index_type, array, first, mid - 1, x)
        else:
            return search(index_type, array, mid + 1, last, x)
    else:
        return [-1, last + 1]


#####       GUARDADO Y CARGA       ######


# Guardado de datos
def save(pictures, nicks, names):
    data = [pictures, nicks, names]
    try:
        f = open("Pictures.pkl", "wb")
        pickle.dump(data, f)
        f.close()
    except:
        print("Hubo un error al guardar el archivo")


# Carga de datos
def load():
    try:
        f = open("Pictures.pkl", "rb")
        data = pickle.load(f)
        f.close()
        return data
    except:
        print("Hubo un error al cargar los datos")
        return False
