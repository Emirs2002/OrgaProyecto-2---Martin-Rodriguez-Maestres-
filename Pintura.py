class Pintura:
    def __init__(self, cota, nombre, precio, anho, status, exists):
        self.cota = cota
        self.nombre = nombre
        self.precio = precio
        self.anho = anho
        self.status = status
        self.exists = exists

    def showPintura(self):
        print(
            f"""-Cota: {self.cota}
                \n-Nombre: {self.nombre}
                \n-Precio: ${self.precio}
                \n-Año: {self.anho}
                \n-Status: {self.status}"""
        )

    def changeStatus(self, status):
        if self.status == status:
            print(f"La pintura ya está {(self.status).lower()}")
        else:
            self.status = status
            print(f"La pintura ahora está {(self.status).lower()}")

    def deleteLogical(self, exists):
        if self.exists == exists:
            print("Esta pintura no fue encontrada")
        else:
            self.exists = exists
            print("La pintura se eliminó lógicamente")
