from typing import List, Optional

# Clase Persona
class Persona:
    def __init__(self, nombre: str, apellido: str, sexo: str):
        self._nombre = nombre
        self._apellido = apellido
        self._sexo = sexo
        self._conyuge = None  # Referencia a otra Persona
        self._padres = []  # Lista de padres

    # Métodos para establecer relaciones
    def set_conyuge(self, conyuge: 'Persona'):
        self._conyuge = conyuge

    def agregar_padre(self, padre: 'Persona'):
        self._padres.append(padre)

    # Método para mostrar información
    def mostrar_info(self) -> str:
        conyuge_nombre = self._conyuge._nombre if self._conyuge else "Ninguno"
        padres_nombres = [padre._nombre for padre in self._padres]
        return (f"Persona: {self._nombre} {self._apellido}\n"
                f"Sexo: {self._sexo}\n"
                f"Cónyuge: {conyuge_nombre}\n"
                f"Padres: {', '.join(padres_nombres) if padres_nombres else 'Ninguno'}")

# Configuración y ejecución
def main():
    # Crear instancias de las personas
    kate = Persona("Kate", "Windsor", "Mujer")
    guillermo = Persona("Guillermo", "Windsor", "Hombre")
    diana = Persona("Diana", "Windsor", "Mujer")
    carlos = Persona("Carlos", "Windsor", "Hombre")

    # Establecer relaciones
    kate.set_conyuge(guillermo)
    guillermo.set_conyuge(kate)
    guillermo.agregar_padre(diana)
    guillermo.agregar_padre(carlos)
    diana.set_conyuge(carlos)
    carlos.set_conyuge(diana)

    # Mostrar información de cada persona
    print("Información de las personas:")
    print(kate.mostrar_info())
    print("\n" + guillermo.mostrar_info())
    print("\n" + diana.mostrar_info())
    print("\n" + carlos.mostrar_info())

if __name__ == "__main__":
    main()