import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..')))

from biblioteca_ayed_fiuner.ayedfiuner.estructuras.LDE import ListaDobleEnlazada


class DequeEmptyError(Exception):
    """Excepción que se lanza al intentar sacar una carta de un mazo vacío."""
    pass


class Mazo:
    """TAD Mazo implementado sobre ListaDobleEnlazada. Cabeza=arriba, Cola=abajo."""

    def __init__(self):
        self._cartas = ListaDobleEnlazada()

    def poner_carta_arriba(self, carta):
        self._cartas.agregar_al_inicio(carta)

    def poner_carta_abajo(self, carta):
        self._cartas.agregar_al_final(carta)

    def sacar_carta_arriba(self, mostrar=False):
        if len(self._cartas) == 0:
            raise DequeEmptyError("No se puede sacar una carta de un mazo vacío.")
        carta = self._cartas.extraer(0)
        carta.visible = mostrar
        return carta

    def __len__(self):
        return len(self._cartas)

    def __str__(self):
        return " ".join(str(carta) for carta in self._cartas)

    def __repr__(self):
        return self.__str__()
