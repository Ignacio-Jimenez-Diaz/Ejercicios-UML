from pintura import Pintura
from replica import Replica

def mostrar_diagrama_objetos():
    # Crear objeto para La Gioconda Original
    original = Pintura(
        nombre="La Gioconda",
        autor="Leonardo Da Vinci",
        cronologia="1503-1516",
        tecnica="Óleo",
        subtecnica="Sfumato",
        material="Madera de álamo",
        ubicacion="Museo Louvre (París)",
        conservacion="Peor que la réplica"
    )

    # Crear objeto para la Réplica
    replica = Replica(
        nombre="Réplica de La Gioconda",
        autor="Anónimo (alumno de Leonardo)",
        cronologia="1503-1516",
        tecnica="Óleo",
        subtecnica="Pincelada simple",
        material="Madera de nogal",
        ubicacion="Museo del Prado (Madrid)",
        conservacion="Mucho mejor que la original",
        procedencia="Colecciones Reales",
        original=original
    )

    # Mostrar información
    print("=== Diagrama de Objetos: Pinturas ===")
    print(original.mostrar_info())
    print("\n" + "="*40 + "\n")
    print(replica.mostrar_info())

if __name__ == "__main__":
    mostrar_diagrama_objetos()