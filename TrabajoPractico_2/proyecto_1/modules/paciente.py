"""
Módulo de dominio: Paciente para la Sala de Emergencias.
"""

from dataclasses import dataclass, field
from itertools import count

_contador_global = count(1)


class NivelRiesgoInvalidoError(ValueError):
    """El nivel de riesgo debe ser 1, 2 o 3."""
    pass


@dataclass
class Paciente:
    """
    Representa un paciente en el sistema de triaje.

    nivel_riesgo: 1=crítico, 2=moderado, 3=bajo
    turno: se asigna automáticamente según el orden de llegada
    """

    nombre: str
    nivel_riesgo: int
    turno: int = field(default_factory=lambda: next(_contador_global), init=False)

    def __post_init__(self):
        if self.nivel_riesgo not in (1, 2, 3):
            raise NivelRiesgoInvalidoError(
                f"Nivel de riesgo inválido: {self.nivel_riesgo}. Debe ser 1, 2 o 3."
            )

    def __lt__(self, otro):
        # primero por nivel de riesgo, ante empate por orden de llegada
        if self.nivel_riesgo != otro.nivel_riesgo:
            return self.nivel_riesgo < otro.nivel_riesgo
        return self.turno < otro.turno

    def __eq__(self, otro):
        if not isinstance(otro, Paciente):
            return NotImplemented
        return self.nivel_riesgo == otro.nivel_riesgo and self.turno == otro.turno

    def __repr__(self):
        niveles = {1: "CRÍTICO", 2: "MODERADO", 3: "BAJO"}
        return f"Paciente('{self.nombre}', riesgo={niveles[self.nivel_riesgo]}, turno={self.turno})"
