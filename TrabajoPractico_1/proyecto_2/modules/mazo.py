import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..')))

from biblioteca_ayed_fiuner.ayedfiuner.estructuras.LDE import ListaDobleEnlazada


class DequeEmptyError(Exception):
    """Excepción que se lanza al intentar sacar una carta de un mazo vacío."""
    pass


class Mazo:
    """
    TAD Mazo de cartas implementado sobre una ListaDobleEnlazada.

    La 'parte de arriba' del mazo corresponde a la CABEZA de la LDE.
    La 'parte de abajo' del mazo corresponde a la COLA de la LDE.

    Invariante de clase:
        - len(self) >= 0
        - Todas las operaciones sobre el mazo se realizan exclusivamente
          por los extremos (arriba o abajo), nunca por posiciones intermedias.
        - Si len(self) == 0, el mazo está vacío y no se puede sacar ninguna carta.
        - Si len(self) > 0, existe exactamente una carta en la posición superior
          y una en la posición inferior (pueden ser la misma si len == 1).
    """

    def __init__(self):
        """
        Inicializa el mazo vacío.

        Postcondición: len(self) == 0
        """
        self._cartas = ListaDobleEnlazada()

    def poner_carta_arriba(self, carta):
        """
        Agrega una carta en la parte superior del mazo.

        Precondición: carta es un objeto de tipo Carta (no None).
        Postcondición: len(self) == len(self_antes) + 1
                       La carta queda en la posición superior del mazo.
                       El resto de las cartas mantiene su orden relativo.
        Complejidad: O(1).
        """
        self._cartas.agregar_al_inicio(carta)

    def poner_carta_abajo(self, carta):
        """
        Agrega una carta en la parte inferior del mazo.

        Precondición: carta es un objeto de tipo Carta (no None).
        Postcondición: len(self) == len(self_antes) + 1
                       La carta queda en la posición inferior del mazo.
                       El resto de las cartas mantiene su orden relativo.
        Complejidad: O(1).
        """
        self._cartas.agregar_al_final(carta)

    def sacar_carta_arriba(self, mostrar=False):
        """
        Extrae y devuelve la carta de la posición superior del mazo.

        Precondición: len(self) > 0  (el mazo no está vacío)
                      mostrar es un valor booleano.
        Postcondición: len(self) == len(self_antes) - 1
                       El valor retornado es la carta que estaba en la posición
                       superior antes de la extracción.
                       Si mostrar == True, la carta retornada tiene visible == True.
                       Si mostrar == False, la carta retornada tiene visible == False.
                       El orden del resto de las cartas no se modifica.
        Lanza DequeEmptyError si len(self) == 0.
        Complejidad: O(1).
        """
        if len(self._cartas) == 0:
            raise DequeEmptyError("No se puede sacar una carta de un mazo vacío.")
        carta = self._cartas.extraer(0)
        carta.visible = mostrar
        return carta

    def __len__(self):
        """
        Devuelve la cantidad de cartas en el mazo.

        Postcondición: retorno >= 0
                       retorno == cantidad de cartas actualmente en el mazo.
        Complejidad: O(1).
        """
        return len(self._cartas)

    def __str__(self):
        """
        Devuelve una representación en cadena de todas las cartas del mazo,
        de la posición superior a la inferior, separadas por espacios.

        Postcondición: retorno es una cadena de texto.
                       Si len(self) == 0, retorno == ''.
        """
        return " ".join(str(carta) for carta in self._cartas)

    def __repr__(self):
        return self.__str__()