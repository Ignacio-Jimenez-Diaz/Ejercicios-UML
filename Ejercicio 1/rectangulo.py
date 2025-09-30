from figura import Figura
import math
import math

class Rectangulo(Figura):
    def __init__(self, longitud: float, anchura: float, color: str = "naranja"):
        super().__init__()
        self._longitud = longitud
        self._anchura = anchura
        self._color = color

    def area(self) -> float:
        return self._longitud * self._anchura

    def get_longitud(self) -> float:
        return self._longitud

    def get_anchura(self) -> float:
        return self._anchura

    def get_color(self) -> str:
        return self._color