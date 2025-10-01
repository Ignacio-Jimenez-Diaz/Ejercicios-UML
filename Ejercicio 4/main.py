from catedral import Catedral

def mostrar_diagrama_objetos():
    # Crear objeto para la Catedral de Santiago
    catedral = Catedral(
        nombre="Catedral de Santiago de Compostela",
        tipo="Templo de culto católico",
        ubicacion="Santiago de Compostela, La Coruña, Galicia, España",
        material="Granito",
        inicio_construccion=1075,
        ultima_piedra=1122,
        consagracion_inicial=1128,
        ultima_etapa=1168,
        consagracion_definitiva="3 de abril de 1211",
        estilos=["Románico", "Gótico", "Barroco", "Plateresco", "Neoclásico"],
        declaracion="Bien de Interés Cultural (1896)"
    )

    # Mostrar información
    print("=== Diagrama de Objetos: Catedral de Santiago ===")
    print(catedral.mostrar_info())

if __name__ == "__main__":
    mostrar_diagrama_objetos()