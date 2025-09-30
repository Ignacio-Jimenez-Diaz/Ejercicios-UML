from typing import List, Optional

# Clase Persona
class Persona:
    def __init__(self, nombre: str, apellido: str, apellido_nacimiento: str):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__apellido_nacimiento = apellido_nacimiento
        self.__conyuge = None  # Referencia a otra Persona (puede ser nulo)
        self.__padres = []  # Lista de padres (puede estar vacía)
    
    # Getters
    def get_nombre(self) -> str:
        return self.__nombre
    
    def get_apellido(self) -> str:
        return self.__apellido
    
    def get_apellido_nacimiento(self) -> str:
        return self.__apellido_nacimiento
    
    def get_conyuge(self) -> Optional['Persona']:
        return self.__conyuge
    
    def get_padres(self) -> List['Persona']:
        return self.__padres
    
    # Setters
    def set_nombre(self, nombre: str):
        self.__nombre = nombre
    
    def set_apellido(self, apellido: str):
        self.__apellido = apellido
    
    def set_apellido_nacimiento(self, apellido_nacimiento: str):
        self.__apellido_nacimiento = apellido_nacimiento
    
    def set_conyuge(self, conyuge: Optional['Persona']):
        self.__conyuge = conyuge
    
    def agregar_padre(self, padre: 'Persona'):
        self.__padres.append(padre)
    
    # Método para mostrar información
    def mostrar_info(self) -> str:
        conyuge_nombre = self.__conyuge.get_nombre() if self.__conyuge else "Ninguno"
        padres_nombres = [padre.get_nombre() for padre in self.__padres]
        return (f"Persona: {self.__nombre} {self.__apellido} "
                f"(Nacida: {self.__apellido_nacimiento})\n"
                f"Cónyuge: {conyuge_nombre}\n"
                f"Padres: {', '.join(padres_nombres) if padres_nombres else 'Ninguno'}")

# Configuración y ejecución
def main():
    # Crear instancias de las personas
    kate = Persona("Kate", "Windsor", "Middleton")
    guillermo = Persona("Guillermo", "Windsor", "Windsor")
    carlos = Persona("Carlos", "Windsor", "Windsor")
    diana = Persona("Diana", "Windsor", "Spencer")
    
    # Establecer relaciones
    kate.set_conyuge(guillermo)
    guillermo.set_conyuge(kate)
    guillermo.agregar_padre(carlos)
    guillermo.agregar_padre(diana)
    
    # Mostrar información de cada objeto
    print(kate.mostrar_info())
    print("\n" + guillermo.mostrar_info())
    print("\n" + carlos.mostrar_info())
    print("\n" + diana.mostrar_info())

if __name__ == "__main__":
    main()