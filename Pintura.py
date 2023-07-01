class Pintura:

    def __init__(self, cota, nombre, precio, anho, status, exists):
        self.cota = cota
        self.nombre = nombre
        self.precio = precio
        self.anho = anho
        self.status = status
        self.exists = exists

    def showPintura(self):
        print(f'''-Cota: {self.cota}
                \n-Nombre: {self.nombre}
                \n-Precio: ${self.precio}
                \n-Año: {self.anho}
                \n-Status: {self.status}
                \n-Existencia: {self.exists}''')

