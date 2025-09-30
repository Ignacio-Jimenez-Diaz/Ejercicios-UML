from typing import List, Optional
import matplotlib.pyplot as plt
import networkx as nx

# Clase Persona
class Persona:
    def __init__(self, nombre: str, apellido: str, apellido_nacimiento: str, sexo: str):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__apellido_nacimiento = apellido_nacimiento
        self.__sexo = sexo
        self.__conyuge = None  # Referencia a otra Persona (puede ser nulo)
        self.__padres = []  # Lista de padres (puede estar vacía)
    
    # Getters
    def get_nombre(self) -> str:
        return self.__nombre
    
    def get_apellido(self) -> str:
        return self.__apellido
    
    def get_apellido_nacimiento(self) -> str:
        return self.__apellido_nacimiento
    
    def get_sexo(self) -> str:
        return self.__sexo
    
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
    
    def set_sexo(self, sexo: str):
        self.__sexo = sexo
    
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
                f"Sexo: {self.__sexo}\n"
                f"Cónyuge: {conyuge_nombre}\n"
                f"Padres: {', '.join(padres_nombres) if padres_nombres else 'Ninguno'}")

# Configuración y ejecución
def main():
    # Crear instancias de las personas
    kate = Persona("Kate", "Windsor", "Middleton", "Mujer")
    guillermo = Persona("Guillermo", "Windsor", "Windsor", "Hombre")
    diana = Persona("Diana", "Windsor", "Spencer", "Mujer")
    carlos = Persona("Carlos", "Windsor", "Windsor", "Hombre")
    
    # Establecer relaciones
    kate.set_conyuge(guillermo)
    guillermo.set_conyuge(kate)
    guillermo.agregar_padre(diana)
    guillermo.agregar_padre(carlos)
    diana.set_conyuge(carlos)
    carlos.set_conyuge(diana)
    
    # Mostrar información textual
    print("Información de los objetos:")
    print(kate.mostrar_info())
    print("\n" + guillermo.mostrar_info())
    print("\n" + diana.mostrar_info())
    print("\n" + carlos.mostrar_info())
    
    # Crear grafo para el diagrama de objetos
    G = nx.DiGraph()
    
    # Agregar nodos (objetos) con etiquetas detalladas
    G.add_node("kate", label=f"kate:Persona\nNombre: {kate.get_nombre()}\nApellido: {kate.get_apellido()}\nNacimiento: {kate.get_apellido_nacimiento()}\nSexo: {kate.get_sexo()}")
    G.add_node("guillermo", label=f"guillermo:Persona\nNombre: {guillermo.get_nombre()}\nApellido: {guillermo.get_apellido()}\nNacimiento: {guillermo.get_apellido_nacimiento()}\nSexo: {guillermo.get_sexo()}")
    G.add_node("diana", label=f"diana:Persona\nNombre: {diana.get_nombre()}\nApellido: {diana.get_apellido()}\nNacimiento: {diana.get_apellido_nacimiento()}\nSexo: {diana.get_sexo()}")
    G.add_node("carlos", label=f"carlos:Persona\nNombre: {carlos.get_nombre()}\nApellido: {carlos.get_apellido()}\nNacimiento: {carlos.get_apellido_nacimiento()}\nSexo: {carlos.get_sexo()}")
    
    # Agregar relaciones
    G.add_edge("kate", "guillermo", label="Está Casado Con")
    G.add_edge("guillermo", "kate", label="Está Casado Con")
    G.add_edge("guillermo", "diana", label="Es Hijo De")
    G.add_edge("guillermo", "carlos", label="Es Hijo De")
    G.add_edge("diana", "carlos", label="Está Casado Con")
    G.add_edge("carlos", "diana", label="Está Casado Con")
    
    # Configurar el diseño del grafo
    pos = {
        "kate": (0, 2),
        "guillermo": (1, 2),
        "diana": (0, 1),
        "carlos": (1, 1)
    }
    
    # Dibujar el grafo
    plt.figure(figsize=(10, 6))
    nx.draw(G, pos, with_labels=False, node_color="lightgreen", node_size=4000, font_size=10)
    
    # Dibujar etiquetas de nodos
    node_labels = nx.get_node_attributes(G, 'label')
    nx.draw_networkx_labels(G, pos, labels=node_labels, font_size=8)
    
    # Dibujar etiquetas de arcos
    edge_labels = nx.get_edge_attributes(G, 'label')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)
    
    plt.title("Diagrama de Objetos")
    plt.axis('off')  # Ocultar ejes
    plt.show()

if __name__ == "__main__":
    main()