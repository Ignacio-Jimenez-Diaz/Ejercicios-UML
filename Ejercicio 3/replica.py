from pintura import Pintura

class Replica(Pintura):
    def __init__(self, nombre, autor, cronologia, tecnica, subtecnica, material, ubicacion, conservacion, procedencia, original):
        super().__init__(nombre, autor, cronologia, tecnica, subtecnica, material, ubicacion, conservacion)
        self.procedencia = procedencia
        self.original = original

    def mostrar_info(self):
        info = super().mostrar_info()
        return (f"{info}\n"
                f"Procedencia: {self.procedencia}\n"
                f"Relación: Copia de '{self.original.nombre}'")