from abc import ABC, abstractmethod

class Persona(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def relaciones(self):
        pass

    @abstractmethod
    def estado_familiar(self):
        pass