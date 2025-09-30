from persona import Persona

class MiembroFamilia(Persona):
    def __init__(self, nombre: str, apellido: str, apellido_nacimiento: str):
        self._nombre = nombre
        self._apellido = apellido
        self._apellido_nacimiento = apellido_nacimiento
        self._conyuge = None
        self._padres = []

    def set_conyuge(self, conyuge: 'MiembroFamilia'):
        self._conyuge = conyuge

    def agregar_padre(self, padre: 'MiembroFamilia'):
        self._padres.append(padre)

    def relaciones(self) -> int:
        relaciones = 0
        if self._conyuge:
            relaciones += 1
        relaciones += len(self._padres)
        return relaciones

    def estado_familiar(self) -> str:
        if self._conyuge and self._padres:
            return "Casado con hijos de padres conocidos"
        elif self._conyuge:
            return "Casado sin padres conocidos"
        elif self._padres:
            return "Soltero con padres conocidos"
        else:
            return "Soltero sin padres conocidos"

    def get_nombre(self) -> str:
        return self._nombre

    def get_apellido(self) -> str:
        return self._apellido

    def get_apellido_nacimiento(self) -> str:
        return self._apellido_nacimiento

    def get_conyuge(self) -> 'MiembroFamilia':
        return self._conyuge

    def get_padres(self) -> list:
        return self._padres