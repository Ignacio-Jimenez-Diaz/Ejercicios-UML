from abc import ABC, abstractmethod
import turtle
import time

# Clase abstracta Figura
class Figura(ABC):
    def __init__(self, color):
        self.__color = color  # Atributo privado
    
    # Getter para color
    def get_color(self):
        return self.__color
    
    # Setter para color
    def set_color(self, color):
        self.__color = color
    
    @abstractmethod
    def dibujar(self, t):
        pass

# Clase Circulo
class Circulo(Figura):
    def __init__(self, color, radio):
        super().__init__(color)
        self.__radio = radio  # Atributo privado
    
    # Getter para radio
    def get_radio(self):
        return self.__radio
    
    # Setter para radio
    def set_radio(self, radio):
        self.__radio = radio
    
    def dibujar(self, t):
        t.fillcolor(self.get_color())
        t.begin_fill()
        t.circle(self.__radio)
        t.end_fill()

# Clase Rectangulo
class Rectangulo(Figura):
    def __init__(self, color, largo, ancho):
        super().__init__(color)
        self.__largo = largo  # Atributo privado
        self.__ancho = ancho  # Atributo privado
    
    # Getter para largo
    def get_largo(self):
        return self.__largo
    
    # Setter para largo
    def set_largo(self, largo):
        self.__largo = largo
    
    # Getter para ancho
    def get_ancho(self):
        return self.__ancho
    
    # Setter para ancho
    def set_ancho(self, ancho):
        self.__ancho = ancho
    
    def dibujar(self, t):
        t.fillcolor(self.get_color())
        t.begin_fill()
        for _ in range(2):
            t.forward(self.__largo)
            t.left(90)
            t.forward(self.__ancho)
            t.left(90)
        t.end_fill()

# Clase Cuadrado
class Cuadrado(Figura):
    def __init__(self, color, lado):
        super().__init__(color)
        self.__lado = lado  # Atributo privado
    
    # Getter para lado
    def get_lado(self):
        return self.__lado
    
    # Setter para lado
    def set_lado(self, lado):
        self.__lado = lado
    
    def dibujar(self, t):
        t.fillcolor(self.get_color())
        t.begin_fill()
        for _ in range(4):
            t.forward(self.__lado)
            t.left(90)
        t.end_fill()

# Clase Ovalo
class Ovalo(Figura):
    def __init__(self, color, radio1, radio2):
        super().__init__(color)
        self.__radio1 = radio1  # Atributo privado
        self.__radio2 = radio2  # Atributo privado
    
    # Getter para radio1
    def get_radio1(self):
        return self.__radio1
    
    # Setter para radio1
    def set_radio1(self, radio1):
        self.__radio1 = radio1
    
    # Getter para radio2
    def get_radio2(self):
        return self.__radio2
    
    # Setter para radio2
    def set_radio2(self, radio2):
        self.__radio2 = radio2
    
    def dibujar(self, t):
        t.fillcolor(self.get_color())
        t.begin_fill()
        t.right(45)  # Rotar para una mejor orientación
        for _ in range(2):
            t.circle(self.__radio1, 90)  # Dibuja arco con radio1
            t.circle(self.__radio2, 90)  # Dibuja arco con radio2
        t.end_fill()
        t.left(45)  # Restaurar orientación

# Configuración de Turtle y ejecución
def main():
    # Inicializar turtle
    t = turtle.Turtle()
    t.speed(5)
    t.pensize(2)
    
    # Crear instancias de las figuras con los colores especificados
    circulo = Circulo("gray", 50)
    rectangulo = Rectangulo("orange", 120, 80)
    cuadrado = Cuadrado("blue", 90)
    ovalo = Ovalo("yellow", 60, 30)
    
    # Dibujar cada figura en diferentes posiciones
    figuras = [circulo, rectangulo, cuadrado, ovalo]
    posiciones = [(-100, 50), (100, 50), (-100, -100), (100, -100)]  # Posiciones para evitar solapamiento
    
    for figura, pos in zip(figuras, posiciones):
        t.penup()
        t.goto(pos)
        t.pendown()
        figura.dibujar(t)
    
    # Mantener la ventana abierta
    time.sleep(5)
    turtle.done()

if __name__ == "__main__":
    main()