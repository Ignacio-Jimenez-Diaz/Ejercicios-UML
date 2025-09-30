from kate import kate
from guillermo import guillermo
from carlos import carlos
from diana import diana

# Establecer relaciones
kate.set_conyuge(guillermo)
guillermo.set_conyuge(kate)
guillermo.agregar_padre(carlos)
guillermo.agregar_padre(diana)

# Mostrar información
def main():
    for persona in [kate, guillermo, carlos, diana]:
        print(f"Persona: {persona.get_nombre()} {persona.get_apellido()} "
              f"(Nacida: {persona.get_apellido_nacimiento()})\n"
              f"Relaciones: {persona.relaciones()}\n"
              f"Estado Familiar: {persona.estado_familiar()}\n")

if __name__ == "__main__":
    main()