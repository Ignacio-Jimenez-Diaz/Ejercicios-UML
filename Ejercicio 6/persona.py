from datetime import datetime

class Persona:
    def __init__(self, nombre, primer_apellido, fecha_nacimiento, sexo, segundo_apellido=None, numero_identificacion=None):
        self.nombre = nombre
        self.primer_apellido = primer_apellido
        self.segundo_apellido = segundo_apellido
        self.fecha_nacimiento = datetime.strptime(fecha_nacimiento, "%Y-%m-%d")
        self.sexo = sexo
        self.numero_identificacion = numero_identificacion

    def mostrar_info(self):
        info = f"Nombre: {self.nombre}\nPrimer apellido: {self.primer_apellido}"
        if self.segundo_apellido:
            info += f"\nSegundo apellido: {self.segundo_apellido}"
        info += f"\nFecha de nacimiento: {self.fecha_nacimiento.strftime('%Y-%m-%d')}\nSexo: {self.sexo}"
        if self.numero_identificacion:
            info += f"\nNúmero de identificación: {self.numero_identificacion}"
        return info