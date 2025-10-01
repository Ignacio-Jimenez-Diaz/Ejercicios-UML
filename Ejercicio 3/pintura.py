class Pintura:
    def __init__(self, nombre, autor, cronologia, tecnica, subtecnica, material, ubicacion, conservacion):
        self.nombre = nombre
        self.autor = autor
        self.cronologia = cronologia
        self.tecnica = tecnica
        self.subtecnica = subtecnica
        self.material = material
        self.ubicacion = ubicacion
        self.conservacion = conservacion

    def mostrar_info(self):
        return (f"Pintura: {self.nombre}\n"
                f"Autor: {self.autor}\n"
                f"Cronología: {self.cronologia}\n"
                f"Técnica: {self.tecnica}\n"
                f"Sub-técnica: {self.subtecnica}\n"
                f"Material de soporte: {self.material}\n"
                f"Ubicación: {self.ubicacion}\n"
                f"Estado de conservación: {self.conservacion}")