class Edificio:
    def __init__(self, nombre, tipo, ubicacion, material, inicio_construccion):
        self.nombre = nombre
        self.tipo = tipo
        self.ubicacion = ubicacion
        self.material = material
        self.inicio_construccion = inicio_construccion

    def mostrar_info(self):
        return (f"Edificio: {self.nombre}\n"
                f"Tipo: {self.tipo}\n"
                f"Ubicación: {self.ubicacion}\n"
                f"Material: {self.material}\n"
                f"Inicio de construcción: {self.inicio_construccion}")