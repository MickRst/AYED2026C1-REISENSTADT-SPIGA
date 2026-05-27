from ayedfiuner.estructuras.LDE import ListaDobleEnlazada


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
        - Todas las operaciones se realizan exclusivamente por los extremos.
        - Si len(self) == 0, el mazo está vacío y no se puede sacar ninguna carta.
        - Si len(self) > 0, existe exactamente una carta en la posición superior
          y una en la posición inferior (pueden ser la misma si len == 1).
    """

    def __init__(self):
        """
        Postcondición: len(self) == 0
        """
        self._cartas = ListaDobleEnlazada()

    def poner_carta_arriba(self, carta):
        """
        Precondición: carta es un objeto de tipo Carta (no None).
        Postcondición: len(self) == len(self_antes) + 1
                       La carta queda en la posición superior del mazo.
        Complejidad: O(1).
        """
        self._cartas.agregar_al_inicio(carta)

    def poner_carta_abajo(self, carta):
        """
        Precondición: carta es un objeto de tipo Carta (no None).
        Postcondición: len(self) == len(self_antes) + 1
                       La carta queda en la posición inferior del mazo.
        Complejidad: O(1).
        """
        self._cartas.agregar_al_final(carta)

    def sacar_carta_arriba(self, mostrar=False):
        """
        Precondición: len(self) > 0
                      mostrar es un valor booleano.
        Postcondición: len(self) == len(self_antes) - 1
                       El valor retornado es la carta que estaba en la posición superior.
                       Si mostrar == True, la carta retornada tiene visible == True.
                       Si mostrar == False, la carta retornada tiene visible == False.
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
        Postcondición: retorno >= 0
        Complejidad: O(1).
        """
        return len(self._cartas)

    def __str__(self):
        return " ".join(str(carta) for carta in self._cartas)

    def __repr__(self):
        return self.__str__()
