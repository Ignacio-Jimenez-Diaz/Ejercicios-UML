from persona import Persona

def mostrar_personas():
    # Crear instancias (objetos) de ejemplo
    persona1 = Persona(
        nombre="Juan",
        primer_apellido="García",
        segundo_apellido="López",
        fecha_nacimiento="1990-05-15",
        sexo="Masculino",
        numero_identificacion="12345678A"
    )
    persona2 = Persona(
        nombre="María",
        primer_apellido="Rodríguez",
        fecha_nacimiento="1985-09-22",
        sexo="Femenino"
    )

    # Mostrar información de cada persona
    print("=== Diagrama de Objetos: Personas ===")
    print("Persona 1:")
    print(persona1.mostrar_info())
    print("\nPersona 2:")
    print(persona2.mostrar_info())

if __name__ == "__main__":
    mostrar_personas()