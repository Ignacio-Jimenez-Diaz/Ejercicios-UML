from edificio import Edificio

class Catedral(Edificio):
    def __init__(self, nombre, tipo, ubicacion, material, inicio_construccion, ultima_piedra, consagracion_inicial, ultima_etapa, consagracion_definitiva, estilos, declaracion):
        super().__init__(nombre, tipo, ubicacion, material, inicio_construccion)
        self.ultima_piedra = ultima_piedra
        self.consagracion_inicial = consagracion_inicial
        self.ultima_etapa = ultima_etapa
        self.consagracion_definitiva = consagracion_definitiva
        self.estilos = estilos
        self.declaracion = declaracion

    def mostrar_info(self):
        info = super().mostrar_info()
        return (f"{info}\n"
                f"Última piedra colocada: {self.ultima_piedra}\n"
                f"Consagración inicial: {self.consagracion_inicial}\n"
                f"Última etapa de construcción: {self.ultima_etapa}\n"
                f"Consagración definitiva: {self.consagracion_definitiva}\n"
                f"Estilos arquitectónicos: {', '.join(self.estilos)}\n"
                f"Declaración: {self.declaracion}")