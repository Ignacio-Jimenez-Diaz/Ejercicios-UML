from figura import Figura
import math
import math

class Cuadrado(Figura):
    def __init__(self, lado: float, color: str = "azul"):
        super().__init__()
        self._lado = lado
        self._color = color

    def area(self) -> float:
        return self._lado * self._lado

    def get_lado(self) -> float:
        return self._lado

    def get_color(self) -> str:
        return self._color