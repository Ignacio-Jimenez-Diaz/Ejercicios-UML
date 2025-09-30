from figura import Figura
import math

class Ovalo(Figura):
    def __init__(self, eje_mayor: float, eje_menor: float, color: str = "amarillo"):
        super().__init__()
        self._eje_mayor = eje_mayor
        self._eje_menor = eje_menor
        self._color = color

    def area(self) -> float:
        a = self._eje_mayor / 2
        b = self._eje_menor / 2
        return math.pi * a * b

    def perimetro(self) -> float:
        a = self._eje_mayor / 2
        b = self._eje_menor / 2
        h = ((a - b) ** 2) / ((a + b) ** 2)
        return math.pi * (a + b) * (1 + (3 * h) / (10 + math.sqrt(4 - 3 * h)))

    def get_eje_mayor(self) -> float:
        return self._eje_mayor

    def get_eje_menor(self) -> float:
        return self._eje_menor

    def get_color(self) -> str:
        return self._color